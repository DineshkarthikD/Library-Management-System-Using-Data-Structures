class Issue:

    def __init__(self, issue_id, book_id, member_id):

        self.issue_id = issue_id
        self.book_id = book_id
        self.member_id = member_id

    def __str__(self):

        return (
            f"Issue ID : {self.issue_id}\n"
            f"Book ID : {self.book_id}\n"
            f"Member ID : {self.member_id}"
        )