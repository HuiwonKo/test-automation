import requests

def test_list_experiments():
    """
    실험 리스트가 정상적으로 응답된다.
    """
    assert 1 == 1

def test_create_experiments():
    """
    실험이 정상적으로 추가된다. 
    (pre-step : 모델 레지스트리에 test_model 이 존재해야 한다.)
    """
    data = {
        "id": "test_experiment",
        "buckets": [{"name": "A", "ratio": "100", "model_name": "test_model", "model_version": "v1"}], 
        "bucketing_seed": "100", 
        "description": "test"
        }
    assert 1 == 2
