import json
from pathlib import Path
from utils.eval_service import get_response_with_context
from Helpers.sessionhistory import clear_session_history

project_root = Path(__file__).parent.parent
dataset_path = project_root / "testdata" / "evals" / "v1_dataset.json"
results_path = project_root / "testdata" / "evals" / "v2_dataset.json"

with open(dataset_path, "r") as f:
    data = json.load(f)

result_dict = []
for item in data:
    query = item["question"]
    session_id = "v1dataset"

    actual_answer, retrieved_chunks = get_response_with_context(query, session_id)
    clear_session_history(session_id)

    result_dict.append({
        "id": item["id"],
        "question": query,
        "retrieved_chunks": retrieved_chunks,
        "actual_answer": actual_answer
    })

    print("Done appending " + item["id"])

with open(results_path, "w") as f:
    json.dump(result_dict, f, indent=4)

