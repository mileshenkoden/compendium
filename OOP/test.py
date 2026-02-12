# --- 1. АБСТРАКЦІЯ (Шаблон) ---
class WebsiteCheck:
    def __init__(self, url: str):
        self.url = url
        
    def check(self):
        raise NotImplementedError("Цей метод треба перевизначити!")

    def __repr__(self):
        return f"Check(url='{self.url}')"

class PingCheck(WebsiteCheck):
     def check(self):
          return f" Pinging [{self.url}]... OK (Status 200)"

class WordSearchCheck(WebsiteCheck):
    def __init__(self, url: str, word: str):
        super().__init__(url) 
        self.word = word

    def check(self):
         return f" Searching for '{self.word}' on {self.url}... Found!"

class Monitor:
    def __init__(self):
        self.checks = [] 

    def add_check(self, check_object):
        self.checks.append(check_object)
    
    def run_all(self):
        print("--- STARTING MONITORING ---")
        for check_obj in self.checks:

            result = check_obj.check()
            print(result)
        print("--- DONE ---")


my_monitor = Monitor()

google_ping = PingCheck("google.com")
facebook_search = WordSearchCheck("facebook.com", "Mark Zuckerberg")
my_site_ping = PingCheck("mysite.com")

my_monitor.add_check(google_ping)
my_monitor.add_check(facebook_search)
my_monitor.add_check(my_site_ping)

my_monitor.run_all()