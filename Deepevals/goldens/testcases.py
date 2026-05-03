from Deepevals.login import run_login
from deepeval.dataset import EvaluationDataset
from utils.eval_service import get_response_with_context
from deepeval.test_case import LLMTestCase
from utils.eval_service import eval_service

dataset=EvaluationDataset()
dataset.pull(alias="Manual Golden Dataset")

test_cases =[]

for golden in dataset.goldens











