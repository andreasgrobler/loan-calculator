from django.db import models
from django.db.models.signals import post_save


class Output(models.Model):
    objects = models.Manager()
    loan_number = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    period = models.IntegerField()
    begin_value = models.FloatField()
    payment_period = models.FloatField()
    interest_period = models.FloatField()
    principal_period = models.FloatField()
    end_value = models.FloatField()


class Input(models.Model):
    objects = models.Manager()
    loan_number = models.AutoField(primary_key=True)
    name_of_loan = models.TextField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
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


    def save(self, *args, **kwargs):
        self.principal = self.price - self.deposit
        self.payment = self.calculate_payment
        super(Input, self).save(*args, **kwargs)


def create_output(sender, instance, *args, **kwargs):

    def amortisation_dictionary(instance):

        begin_balance = instance.principal

        for period in range(1, int(instance.term*12+1)):

            interest_period = (instance.interest_rate/100/12)* begin_balance
            principal_period = instance.payment - interest_period
            end_balance = begin_balance - principal_period

            yield  {
                    'Loan Number': instance.loan_number,
                    'Period': period,
                    'Begin Balance': begin_balance,
                    'Payment': instance.payment,
                    'Principal': principal_period,
                    'Interest': interest_period,
                    'End Balance': end_balance,
                    }

            begin_balance = end_balance

    for record in amortisation_dictionary(instance):
        Output.objects.create (
            loan_number=record['Loan Number'],
            period=record['Period'],
            begin_value=record['Begin Balance'],
            payment_period=record['Payment'],
            principal_period=record['Principal'],
            interest_period=record['Interest'],
            end_value=record['End Balance']
        )


post_save.connect(create_output, sender=Input)