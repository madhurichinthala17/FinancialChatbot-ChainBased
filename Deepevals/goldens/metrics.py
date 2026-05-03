from Deepevals.login import run_login
from Deepevals.goldens.testcases import get_testcases
from deepeval.models import OllamaModel
from deepeval import evaluate
from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    ContextualRelevancyMetric
)

testcases = get_testcases()


evaluate(test_cases=testcases,metrics = [AnswerRelevancyMetric()], identifier="v1")

evaluate(test_cases=testcases,metrics = [FaithfulnessMetric()], identifier="v1")

evaluate(test_cases=testcases,metrics = [ContextualPrecisionMetric()], identifier="v1")

evaluate(test_cases=testcases,metrics = [ContextualRecallMetric()], identifier="v1")

evaluate(test_cases=testcases,metrics = [ContextualRelevancyMetric()], identifier="v1")
