(() => {
    function init() {
        mermaid.initialize({
            startOnLoad: false,
            theme: "default",
            securityLevel: "loose",
            flowchart: { useMaxWidth: true, htmlLabels: true, curve: "basis" },
            mindmap: { useMaxWidth: true },
            timeline: {}
        });
        const TAB_KEY = "selectedTab";
        const DEFAULT_TAB = document.body.dataset.defaultTab || "flowchart";
        const renderQueue = [];
        let isRendering = false;
        const BATCH_SIZE = 2;
        const BATCH_DELAY = 150;
        const tabButtons = [...document.querySelectorAll(".tab-button")];
        const tabContents = [...document.querySelectorAll(".tab-content")];
        const params = new URLSearchParams(window.location.search);
        const storedTab = sessionStorage.getItem(TAB_KEY);
        let initialTab = params.get("tab") || storedTab || DEFAULT_TAB;

        function decodeHtml(text) {
            const textarea = document.createElement("textarea");
            textarea.innerHTML = text;
            return textarea.value;
        }

        function renderDiagram(container, code, id) {
            return new Promise((resolve, reject) => {
                try {
                    const mermaidId = "mermaid-" + id + "-" + Date.now() + "-" + Math.random().toString(36).slice(2, 11);
                    if (typeof mermaid.render === "function") {
                        mermaid.render(mermaidId, code).then(result => {
                            if (result && result.svg) {
                                const temp = document.createElement("div");
                                temp.innerHTML = result.svg;
                                if (temp.querySelector(".error-text, .error-icon")) {
                                    reject(new Error("Syntax error in diagram"));
                                } else {
                                    container.innerHTML = result.svg;
                                    container.className = "mermaid-rendered";
                                    container.style.display = "block";
                                    resolve();
                                }
                            } else {
                                reject(new Error("Invalid render result"));
                            }
                        }).catch(error => reject(error));
                    } else {
                        container.style.display = "block";
                        container.id = mermaidId;
                        container.className = "mermaid";
                        container.textContent = code;
                        if (typeof mermaid.run === "function") {
                            mermaid.run({ nodes: [container], suppressErrors: true }).then(() => {
                                const svg = container.querySelector("svg");
                                const errorDiv = container.querySelector(".error-text");
                                if (svg && !errorDiv) resolve();
                                else reject(new Error("No SVG generated or has errors"));
                            }).catch(error => reject(error));
                        } else if (typeof mermaid.init === "function") {
                            mermaid.init(undefined, [container]);
                            setTimeout(() => {
                                const svg = container.querySelector("svg");
                                const errorDiv = container.querySelector(".error-text");
                                if (svg && !errorDiv) resolve();
                                else reject(new Error("No SVG generated or has errors"));
                            }, 500);
                        } else {
                            mermaid.contentLoaded();
                            setTimeout(() => {
                                const svg = container.querySelector("svg");
                                const errorDiv = container.querySelector(".error-text");
                                if (svg && !errorDiv) resolve();
                                else reject(new Error("No SVG generated or has errors"));
                            }, 500);
                        }
                    }
                } catch (error) {
                    reject(error);
                }
            });
        }

        function processQueue() {
            if (isRendering || renderQueue.length === 0) return;
            isRendering = true;
            const batch = renderQueue.splice(0, BATCH_SIZE);
            let done = 0;
            batch.forEach((item, index) => {
                setTimeout(() => {
                    const container = item.container;
                    renderDiagram(container, item.code, item.id).then(() => {
                        const errors = container.querySelectorAll(".error-text, .error-icon");
                        errors.forEach(el => el.remove());
                    }).catch(() => {
                        const errors = container.querySelectorAll(".error-text, .error-icon, svg");
                        errors.forEach(el => el.remove());
                        container.innerHTML = "";
                        container.className = "mermaid-error-container";
                        container.style.display = "block";
                    }).finally(() => {
                        const skeleton = container.parentElement.querySelector(".skeleton-loader");
                        if (skeleton) skeleton.style.display = "none";
                        done += 1;
                        if (done === batch.length) {
                            isRendering = false;
                            if (renderQueue.length > 0) setTimeout(processQueue, BATCH_DELAY);
                        }
                    });
                }, index * 100);
            });
        }

        function queueContainer(container) {
            const id = container.getAttribute("data-diagram-id");
            let code = container.getAttribute("data-mermaid-code");
            if (!code || container.classList.contains("queued")) return;
            container.classList.add("queued");
            code = decodeHtml(code);
            renderQueue.push({ container, code, id });
            processQueue();
        }

        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    observer.unobserve(entry.target);
                    queueContainer(entry.target);
                }
            });
        }, { root: null, rootMargin: "300px", threshold: 0.01 });

        function updateUrl(tab) {
            const nextParams = new URLSearchParams(window.location.search);
            nextParams.set("tab", tab);
            history.replaceState({}, "", `${window.location.pathname}?${nextParams.toString()}`);
        }

        function activateTab(tab) {
            let button = tabButtons.find(item => item.dataset.tab === tab);
            if (!button) {
                tab = DEFAULT_TAB;
                button = tabButtons.find(item => item.dataset.tab === tab);
            }
            if (!button) return;
            tabButtons.forEach(item => item.classList.remove("active"));
            tabContents.forEach(item => item.classList.remove("active"));
            button.classList.add("active");
            const content = document.getElementById(`${tab}-content`);
            if (content) content.classList.add("active");
            sessionStorage.setItem(TAB_KEY, tab);
            updateUrl(tab);
            requestAnimationFrame(() => {
                document.querySelectorAll(`#${tab}-content .mermaid-container`).forEach(container => {
                    if (!container.classList.contains("queued") && !container.classList.contains("mermaid-rendered")) {
                        observer.observe(container);
                    }
                });
            });
        }

        tabButtons.forEach(button => {
            button.addEventListener("click", event => {
                event.preventDefault();
                if (!button.classList.contains("active")) activateTab(button.dataset.tab);
            });
        });

        function enhanceCards() {
            document.querySelectorAll(".tab-content .card").forEach(card => {
                if (card.dataset.enhanced === "true") return;
                card.dataset.enhanced = "true";
                card.addEventListener("click", () => {
                    const activeTab = sessionStorage.getItem(TAB_KEY) || DEFAULT_TAB;
                    const url = new URL(card.href, window.location.origin);
                    url.searchParams.set("tab", activeTab);
                    card.href = url.toString();
                });
            });
        }

        enhanceCards();
        if (!tabButtons.some(button => button.dataset.tab === initialTab)) initialTab = DEFAULT_TAB;
        activateTab(initialTab);
    }

    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
    else init();
})();
