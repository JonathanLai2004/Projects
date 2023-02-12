existing_messages = [{'has_been_viewed':False, 'from_number':8769038451, 'time':'09:30','date':'2022-10-27','text_of_SMS':'Hi, how about lunch at 11?'},
                        {'has_been_viewed':False, 'from_number':9579038373, 'time':'19:30','date':'2022-10-20', 'text_of_SMS':'Your order has arrived'},
                        {'has_been_viewed':True, 'from_number':8639568726, 'time':'10:30','date':'2022-09-30','text_of_SMS':'Card not present on American Express acc ending 54345 Sep 30 Amount $45.43 Merch: TOMATEFRESHKITCHEN.COM if unrecognized call # on Card'},
                        {'has_been_viewed':False, 'from_number':4567653456, 'time':'11:50','date':'2022-09-15','text_of_SMS':'Hi Brooke, we are confirming your Covid vaccine appointment on Thursday at 1900 hours'},
                        {'has_been_viewed':False, 'from_number':5646786643, 'time':'18:50','date':'2022-09-11','text_of_SMS':'Where is the party bro?'},
                        {'has_been_viewed':False, 'from_number':9845543492, 'time':'17:10','date':'2022-09-10','text_of_SMS':'Free trial of ScanApp for 7 days for clear scanned documents, cancel anytime, $10.99 per month after 7 days'},
                        {'has_been_viewed':True, 'from_number':8793450987, 'time':'13:20','date':'2022-08-31','text_of_SMS':'Hey Brooke, I have sent you my resume for feedback'},
                        {'has_been_viewed':True, 'from_number':874556445, 'time':'07:20','date':'2022-08-19','text_of_SMS':'Which route are we taking for the run today?'},
                        {'has_been_viewed':True, 'from_number':998456435, 'time':'07:20','date':'2022-07-31','text_of_SMS':'Reservation confirmed at the New York Plaza hotel for 2022-08-09 to 2022-09-14.'},
                        {'has_been_viewed':True, 'from_number':8769038451, 'time':'07:20','date':'2022-07-25','text_of_SMS':'Lets catchup sometime, it has been so long!'},
                        {'has_been_viewed':True, 'from_number':7739984533, 'time':'07:20','date':'2022-07-24','text_of_SMS':'Do you want to be rich today? Do you want to be your own boss? Check out beyourownboss.com. Register today for just $5!!!'},
                        {'has_been_viewed':True, 'from_number':3443498738, 'time':'07:20','date':'2022-07-22','text_of_SMS':'Want to lose weight? Get Dr. Oz magic pills @ozpills.com. Satisfaction guaranteed.'}]

class SMS_store_manager:
    
    def __init__(self, existing_messages):
        self.messages = existing_messages
        
    def add_new_arrival(self, from_number, time_arrived, date, text_of_SMS):
        self.messages.append({'has_been_viewed':False,'from_number':from_number,'time':time_arrived,'date':date,'text_of_SMS':text_of_SMS})
        # creates a new dictionary entry from arguments entered, then appending it to the list of other messages.
        
    def message_count(self):
        return len(self.messages)
        # returns the length of the list of messages

    def get_unread_messages(self):
        for i in range(len(self.messages)):
            if self.messages[i]['has_been_viewed'] == False:
                self.messages[i]['has_been_viewed'] = True
                for j in ['from_number','time','date','text_of_SMS']:
                    print(self.messages[i][j])
                print(' ')
        # if the message hasn't been viewed, changes the status to viewed and prints the message

    def delete(self, i):
        self.messages.pop(i)
        # deletes a message by index
    
    def clear(self):
        self.messages.clear()
        # clears the list of messages

harry_messages = SMS_store_manager(existing_messages)

harry_messages.add_new_arrival(8749373884,'07:25','2022-10-29','Hey, I want my bike back.')

harry_messages.message_count()

harry_messages.get_unread_messages()

harry_messages.get_unread_messages()

harry_messages.clear()

harry_messages.message_count()

# ------------------------------
# new version of SMS manager
# ------------------------------

#Lists for initializing the attributes of the class
existing_messages = [{'has_been_viewed':False, 'from_number':8769038451, 'time':'09:30','date':'2022-10-27','text_of_SMS':'Hi, how about lunch at 11?'},
                        {'has_been_viewed':False, 'from_number':9579038373, 'time':'19:30','date':'2022-10-20', 'text_of_SMS':'Your order has arrived'},
                        {'has_been_viewed':True, 'from_number':8639568726, 'time':'10:30','date':'2022-09-30','text_of_SMS':'Card not present on American Express acc ending 54345 Sep 30 Amount $45.43 Merch: TOMATEFRESHKITCHEN.COM if unrecognized call # on Card'},
                        {'has_been_viewed':False, 'from_number':4567653456, 'time':'11:50','date':'2022-09-15','text_of_SMS':'Hi Brooke, we are confirming your Covid vaccine appointment on Thursday at 1900 hours'},
                        {'has_been_viewed':False, 'from_number':5646786643, 'time':'18:50','date':'2022-09-11','text_of_SMS':'Where is the party bro?'},
                        {'has_been_viewed':False, 'from_number':9845543492, 'time':'17:10','date':'2022-09-10','text_of_SMS':'Free trial of ScanApp for 7 days for clear scanned documents, cancel anytime, $10.99 per month after 7 days'},
                        {'has_been_viewed':True, 'from_number':8793450987, 'time':'13:20','date':'2022-08-31','text_of_SMS':'Hey Brooke, I have sent you my resume for feedback'},
                        {'has_been_viewed':True, 'from_number':874556445, 'time':'07:20','date':'2022-08-19','text_of_SMS':'Which route are we taking for the run today?'},
                        {'has_been_viewed':True, 'from_number':998456435, 'time':'07:20','date':'2022-07-31','text_of_SMS':'Reservation confirmed at the New York Plaza hotel for 2022-08-09 to 2022-09-14.'},
                        {'has_been_viewed':True, 'from_number':8769038451, 'time':'07:20','date':'2022-07-25','text_of_SMS':'Lets catchup sometime, it has been so long!'},
                        {'has_been_viewed':True, 'from_number':7739984533, 'time':'07:20','date':'2022-07-24','text_of_SMS':'Do you want to be rich today? Do you want to be your own boss? Check out beyourownboss.com. Register today for just $5, or book an appointment at 985-998-3452!!!'},
                        {'has_been_viewed':True, 'from_number':3443498738, 'time':'07:20','date':'2022-07-22','text_of_SMS':'Want to lose weight? Get Dr. Oz magic pills @ozpills.com. Satisfaction guaranteed.'}]
spam_words=['100% more', '100% free', '100% satisfied', 'Additional income', 'Be your own boss', 'Best price', 'Big bucks', 'Billion', 'Cash bonus', 'Cents on the dollar', 'Consolidate debt', 'Double your cash', 'Double your income', 'Earn extra cash', 'Earn money', 'Eliminate bad credit', 'Extra cash', 'Extra income', 'Expect to earn', 'Fast cash', 'Financial freedom', 'Free access', 'Free consultation', 'Free gift', 'Free hosting', 'Free info', 'Free investment', 'Free membership', 'Free money', 'Free preview', 'Free quote', 'Free trial', 'Full refund', 'Get out of debt', 'Get paid', 'Giveaway', 'Guaranteed', 'Increase sales', 'Increase traffic', 'Incredible deal', 'Lower rates', 'Lowest price', 'Make money', 'Million dollars', 'Miracle', 'Money back', 'Once in a lifetime', 'One time', 'Pennies a day', 'Potential earnings', 'Prize', 'Promise', 'Pure profit', 'Risk-free', 'Satisfaction guaranteed', 'Save big money', 'Save up to', 'Special promotion']
update_words = ['Your order', 'appointment', 'Reservation confirmed', 'Card Not Present', 'Payment confirmation', 'Your payment']

# new class that inherits from SMS_store_manager
class SMS_personalized_store_manager(SMS_store_manager):
    
    def __init__(self, existing_messages, spam_words, update_words):
        self.messages = existing_messages
        self.spam_words = spam_words
        self.update_words = update_words
        
        for i in range(len(self.messages)):                   # first defaults every message to 'personal'
            self.messages[i]['tag'] = 'personal'
        for i in range(len(self.messages)):                   # then, iterating through each message
            for spamword in self.spam_words:                  # check for spam words
                if spamword.lower() in self.messages[i]['text_of_SMS'].lower(): 
                    self.messages[i]['tag'] = 'spam'                   
                    break                                               
                else:                                         # if not tagged as spam
                    for updateword in self.update_words:      # check for update words
                        if updateword.lower() in self.messages[i]['text_of_SMS'].lower():
                            self.messages[i]['tag'] = 'update'
                            break

    def add_new_arrival(self, from_number, time_arrived, date, text_of_SMS):
        self.messages.append({'has_been_viewed':False,'from_number':from_number,'time':time_arrived,'date':date,'text_of_SMS':text_of_SMS})
        self.messages[-1]['tag'] = 'personal'              # after defaulting new message entry as 'personal' 
        for spamword in self.spam_words:                   # check for spam words
            if spamword.lower() in self.messages[-1]['text_of_SMS'].lower():
                self.messages[-1]['tag'] = 'spam'
                break
            else:                                          # if not tagged as spam
                for updateword in self.update_words:       # check for update words
                    if updateword.lower() in self.messages[-1]['text_of_SMS'].lower():
                        self.messages[-1]['tag'] = 'update'
                        break

    def get_unread_messages_by_category(self,category=0):
        if category == 0:                                     # if category isn't specified
            for i in range(len(self.messages)):               # return all the unread messages of any category 
                if self.messages[i]['has_been_viewed'] == False:
                    self.messages[i]['has_been_viewed'] = True
                    for j in ['from_number','time','date','text_of_SMS']:
                        print(self.messages[i][j])
                    print(' ')
        else:                                                 # if category is specified
            for i in range(len(self.messages)):               # return all the unread messages of that specific category
                if self.messages[i]['has_been_viewed'] == False:
                    if self.messages[i]['tag'] == category:
                        self.messages[i]['has_been_viewed'] = True
                        for j in ['from_number','time','date','text_of_SMS']:
                            print(self.messages[i][j])
                        print(' ')
                        
    def get_messages_by_category(self,category=0):
        if category == 0:                                     # if category isn't specified
            for i in range(len(self.messages)):               # return all the messages of any category
                for j in ['from_number','time','date','text_of_SMS']:
                    print(self.messages[i][j])
                print(' ')
        else:                                                 # if category is specified
            for i in range(len(self.messages)):               # return all the messages of that category
                if self.messages[i]['tag'] == category:
                    for j in ['from_number','time','date','text_of_SMS']:
                        print(self.messages[i][j])
                    print(' ')

ron_messages = SMS_personalized_store_manager(existing_messages, spam_words, update_words)

ron_messages.messages

ron_messages.add_new_arrival(8749373884, '07:25','2022-10-29','Hey, I want my bike back.')

ron_messages.get_unread_messages_by_category('personal')

ron_messages.get_unread_messages_by_category('update')

ron_messages.get_unread_messages()

ron_messages.get_messages_by_category('spam')

ron_messages.get_messages_by_category('update')