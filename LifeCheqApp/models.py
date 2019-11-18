from django.db import models


class OutModel(models.Model):
    objects = models.Manager()
    loan_number = models.IntegerField()
    period = models.IntegerField()
    begin_value = models.FloatField()
    payment_period = models.FloatField()
    interest_period = models.FloatField()
    principal_period = models.FloatField()
    end_value = models.FloatField()

class InModel(models.Model):
    objects = models.Manager()
    loan_number = models.IntegerField(primary_key=True)
    name_of_loan = models.TextField(max_length=150)
    price = models.FloatField()
    deposit = models.FloatField()
    term = models.FloatField()
    interest_rate = models.FloatField()
    principal = models.FloatField()
    payment = models.FloatField()

    
    @property
    def calculate_payment(self):
        payment = (self.interest_rate/100/12) / (1 - (1+self.interest_rate/100/12)**-(self.term*12)) * (self.principal)
        return payment
    
    @property
    def amortisation_dictionary(self, *args, **kwargs):

        begin_balance = self.principal

        for period in range(1, int(self.term*12+1)):

            interest_period = (self.interest_rate/100/12)* begin_balance
            principal_period = self.payment - interest_period
            end_balance = begin_balance - principal_period

            yield  {
                    'Loan Number': self.pk,
                    'Period': period,
                    'Begin Balance': begin_balance,
                    'Payment': self.payment,
                    'Principal': principal_period,
                    'Interest': interest_period,
                    'End Balance': end_balance,
                    }

            begin_balance = end_balance


    def save(self, *args, **kwargs):
        
        self.principal = self.price - self.deposit
        
        self.payment = self.calculate_payment
        
        for record in self.amortisation_dictionary:
            OutModel.objects.create(
                loan_number=record['Loan Number'],
                period=record['Period'],
                begin_value=record['Begin Balance'],
                payment=record['Payment'],
                principal_period=record['Principal'],
                interest_period=record['Interest'],
                end_value=record['End Balance'])

        super(InModel, self).save(*args, **kwargs)