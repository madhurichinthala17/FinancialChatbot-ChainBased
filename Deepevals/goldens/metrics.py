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

evaluate(test_cases=testcases,metrics = [FaithfulnessMetric(model=model)], identifier="v1")

evaluate(test_cases=testcases,metrics = [ContextualPrecisionMetric(model=model)], identifier="v1")

evaluate(test_cases=testcases,metrics = [ContextualRecallMetric(model=model)], identifier="v1")

evaluate(test_cases=testcases,metrics = [ContextualRelevancyMetric(model=model)], identifier="v1")
