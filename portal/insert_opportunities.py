from oportal.models import Opportunity, Company

"""
Populates database with a company and multiple opportunities programmatically
"""
def populate():
    company = Company(name="UP CAPES", logo = None)
    opp = Opportunity(role="UI/UX Designer", status="New", location="Local", opportunity_type="INTERNSHIP", duration="August - September", company=company)
    company.save()
    opp.save()
    Opportunity.objects.bulk_create([
        Opportunity(role="Tech Lead", status="New", location="International", opportunity_type="INTERNSHIP", duration="August - September", description='', company=company),
        Opportunity(role="Junior Web Developer", status="Closing Soon", location="Local", opportunity_type="EMPLOYMENT", duration="August - September", company=company),
        Opportunity(role="Senior Web Developer", status="Closing Soon", location="International", opportunity_type="EMPLOYMENT", duration="August - September", company=company),
        Opportunity(role="DevOps Engineer", status="Expired", location="Local", opportunity_type="ACADEME", duration="August - September", company=company),
        Opportunity(role="QA Engineer", status="Expired", location="International", opportunity_type="ACADEME", duration="August - September", company=company),
    ])

populate()