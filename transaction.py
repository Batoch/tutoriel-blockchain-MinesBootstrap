from key import verify_signature


class Transaction:

    def __init__(self, amount, receiver, sender, timestamp = 0, tx_number = None):
        self.amount = amount
        self.receiver = receiver
        self.sender = sender
        self.timestamp = timestamp
        self.tx_number = tx_number

    def __repr__(self):
        string = "Transaction number: " + str(self.tx_number) + "\n" + "Sender: " + str(self.sender) + "\n" + "Receiver: " + str(self.receiver) + "\n" + "Amount: " + str(self.amount) + "\n" + "Timestamp: " + str(self.timestamp) + "\n"
        return string

    def to_dict(self):
        tx_dict = {}
        tx_dict["tx_number"] = self.tx_number
        tx_dict["sender"] = self.sender
        tx_dict["receiver"] = self.receiver
        tx_dict["amount"] = self.amount
        tx_dict["timestamp"] = self.timestamp
        return tx_dict
    pass
