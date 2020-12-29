from trainingcorpus import TrainingCorpus
import email.message

def show_mailer_services_used(corpus_dir):
    ham_mailer_services = dict()
    spam_mailer_services = dict()
    t_corpus = TrainingCorpus(corpus_dir)
    
    for name, mail in t_corpus.emails():
        mailing_service = email.message_from_string(mail).get('X-Mailer')
        if mailing_service:
            if t_corpus.is_ham(name):
                ham_mailer_services[mailing_service] = ham_mailer_services.get(mailing_service, 0) + 1
            else:
                spam_mailer_services[mailing_service] = spam_mailer_services.get(mailing_service, 0) + 1
     
    print("Ham services")
    for key, val in ham_mailer_services.items():
        print(key, val)

    print()
    print("Spam services")
    for key, val in spam_mailer_services.items():
        print(key, val)
