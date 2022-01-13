from datetime import datetime
from notifier.utils import notify_changes
from entities import Company, Event, CompanyCompetitor, Webinar, CRAWLING_STATUSES

old_company = Company(employees_min=1, employees_max=5, is_deleted=False, link="test", name="Test")
new_company = Company(employees_min=2, employees_max=5, is_deleted=True, link="test", name="Test")

old_event = Event(start_date=datetime.now(), link="test", name="Test")

old_webinar = Webinar(start_date=datetime.now(), link="test", name="Test",
                      crawling_status=CRAWLING_STATUSES.TEXT_ANALYZED)
new_webinar = Webinar(start_date=datetime.now(), link="test", name="Test",
                      crawling_status=CRAWLING_STATUSES.TEXT_UPLOADED)

old_company_competitor = CompanyCompetitor(company=old_company, competitor=old_company, is_deleted=False)
new_company_competitor = CompanyCompetitor(company=old_company, competitor=old_company, is_deleted=True)

# Company change
print("------------- Company -------------")
print(notify_changes(new_company, old_company, "Company"))
# Event change
print("------------- Event -------------")
print(notify_changes(None, old_event, "Event"))
# Webinar change
print("------------- Webinar -------------")
print(notify_changes(new_webinar, old_webinar, "Webinar"))
# Company Competitor change
print("------------- Company Competitor -------------")
print(notify_changes(new_company_competitor, old_company_competitor, "CompanyCompetitor"))
# All attributes are missing
print("------------- All attributes are missing -------------")
try:
    print(notify_changes(None, None, None))
except Exception as e:
    print(e)
# entity_obj and original_entity_obj are missing
print("------------- entity_obj and original_entity_obj are missing -------------")
try:
    print(notify_changes(None, None, "Webinar"))
except Exception as e:
    print(e)
