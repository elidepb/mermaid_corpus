import json
import os
import subprocess
import tempfile

def has_syntax_errors(mermaid_code: str) -> bool:
    if not mermaid_code or not mermaid_code.strip():
        return True
    
    tmp_output = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.svg', delete=False) as tmp_file:
            tmp_output = tmp_file.name
        
        try:
            process = subprocess.run(
                [
                    "npx",
                    "--yes",
                    "-p",
                    "@mermaid-js/mermaid-cli",
                    "mmdc",
                    "--input",
                    "-",
                    "--output",
                    tmp_output,
                    "--backgroundColor",
                    "transparent",
                ],
                input=mermaid_code,
                text=True,
                capture_output=True,
                timeout=30,
            )
            
            if process.returncode != 0:
                error_output = process.stderr or ""
                if any(keyword in error_output.lower() for keyword in ["error", "failed", "invalid", "parse"]):
                    return True
            
            if not os.path.exists(tmp_output):
                return True
                
            file_size = os.path.getsize(tmp_output)
            if file_size == 0:
                return True
            
            try:
                with open(tmp_output, 'r', encoding='utf-8') as f:
                    svg_content = f.read()
                    if '<svg' not in svg_content.lower():
                        return True
                    if any(keyword in svg_content.lower() for keyword in ["error", "failed", "invalid"]):
                        return True
            except Exception:
                return True
                
            return False
        finally:
            if tmp_output:
                try:
                    if os.path.exists(tmp_output):
                        os.unlink(tmp_output)
                except Exception:
                    pass
    except FileNotFoundError:
        return True
    except subprocess.TimeoutExpired:
        return True
    except Exception:
        return True

def main():
    errors = {}
    data_path = "flowchart"
    for root, _, files in os.walk(data_path):
        if "jsons" in root:
            for file in files:
                if file.endswith(".json"):
                    filepath = os.path.join(root, file)
                    with open(filepath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    for diagram_data in data.get("diagrams", []):
                        diagram_id = diagram_data["id"]
                        mermaid_code = diagram_data["mermaid_code"]
                        errors[diagram_id] = has_syntax_errors(mermaid_code)

    with open("src/diagram_errors.json", "w") as f:
        json.dump(errors, f)

if __name__ == "__main__":
    main()
