from datetime import datetime, timezone
from fsrs import FSRS, Card, Rating


class QuizScheduler ():
    def __init__ (
        self, 
        datetime_now = None,
        user_id = None,
        course_id = None,
        Topic_id = None,
        quiz_id = None,
    ):
        pass

    # fix this soon
    def test_eval (
        self, 
        ratings = None # get from db
    ):
        fsrs = FSRS()
        card = Card()

        ratings = (
            Rating.Good,
            Rating.Good,
            Rating.Good,
            Rating.Good,
            Rating.Good,
        )

        now = datetime(2022, 11, 29, 12, 30, 0, 0, tzinfo=timezone.utc)
        logs = []
        
        for rating in ratings:
            scheduling_cards = fsrs.repeat(card, now)
            card = scheduling_cards[rating].card
            log = scheduling_cards[rating].review_log
            log = vars(log)
            logs.append(log)
            now = card.due

        last_log = logs[-1]
        return last_log
    
    # getter
    def get_review_date (self):
        log = self.test_eval()
        return log['review']




    