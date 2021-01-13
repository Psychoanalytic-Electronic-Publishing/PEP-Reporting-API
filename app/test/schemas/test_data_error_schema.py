from pytest import fixture

from app.main.schema.data_error_schema import DataErrorSchema


@fixture
def schema() -> DataErrorSchema:
    return DataErrorSchema()


def test_DataErrorSchema_create(schema: DataErrorSchema):
    assert schema

def test_DataErrorSchema_works(schema: DataErrorSchema):
    params = schema.load(
        {
            "data": {
                "type": "dataErrors",
                "attributes": {
                    "username": "OvaltineJenkins",
                    "email": "ovaltine.jenkins@gmail.com",
                    "fullName": "Ovaltine Jenkins",
                    "problemText": "bad",
                    "correctedText": "good",
                    "urlProblemPage": "",
                    "isAuthorPublisher": "false",
                    "hasOriginalCopy": "true"
                }
            }
        }
    )

    assert params['username'] == "OvaltineJenkins"
    assert params['email'] == "ovaltine.jenkins@gmail.com"
    assert params['full_name'] == "Ovaltine Jenkins"
    assert params['problem_text'] == "bad"
    assert params['corrected_text'] == "good"
    assert params['url_problem_page'] == ""
    assert params['is_author_publisher'] is False
    assert params['has_original_copy'] is True
