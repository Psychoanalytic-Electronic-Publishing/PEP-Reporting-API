from pytest import fixture

from app.main.schema.feedback_schema import FeedbackSchema


@fixture
def schema() -> FeedbackSchema:
    return FeedbackSchema()


def test_FeedbackSchema_create(schema: FeedbackSchema):
    assert schema

def test_FeedbackSchema_works(schema: FeedbackSchema):
    params = schema.load(
        {
            "data": {
                "type": "feedbacks",
                "attributes": {
                    "subject": "test subject",
                    "description": "test description",
                    "url": "https://test.com",
                    "feedbackType": "ISSUE",
                    "browser": "firefox",
                    "reporterName": "test name"
                }
            }
        }
    )

    assert params['subject'] == "test subject"
    assert params['description'] == "test description"
    assert params['url'] == "https://test.com"
    assert params['feedback_type'] == "ISSUE"
    assert params['browser'] == "firefox"
    assert params['reporter_name'] == "test name"

