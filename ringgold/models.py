from django.db import models

field_mappings = [
    ('city','city'),
    ('country','country_code'),
    ('region','region'),
    ('value','name'),
    ('disambiguatedAffiliationIdentifier', 'ringgold_id'),
    ('countryForDisplay', 'country_name'),
    ('orgType', 'org_type'),
]

class RinggoldRecord(models.Model):
    city = models.CharField(max_length=512, null=True)
    country_code = models.CharField(max_length=8, null=True)
    country_name = models.CharField(max_length=512, null=True)
    org_type = models.CharField(max_length=128, null=True)
    region = models.CharField(max_length=512, null=True)
    name = models.CharField(max_length=1024)
    ringgold_id = models.IntegerField(unique=True)

    @classmethod
    def from_orcid_json(cls, json):
        """
        Creates a RinggoldRecord from a JSON payload
        returned by ORCID's autocompletion.
        """
        dct = {
            key:json.get(orcid_key)
            for orcid_key, key in field_mappings
        }
        return cls(**dct)

    def to_orcid_json(self):
        """
        Converts the record to ORCID's format
        """
        dct = {
            orcid_key:getattr(self, key)
            for orcid_key, key in field_mappings
        }
        return dct

    @classmethod
    def import_dump(cls, fname):
        """
        Imports a dump of ORCID's JSON autocompletion payloads
        """
        import json
        batch_size = 1000
        with open(fname, 'r') as f:
            batch = []
            for line in f:
                js = json.loads(line.strip())
                rec = cls.from_orcid_json(js)
                batch.append(rec)
                if len(batch) >= batch_size:
                    cls.objects.bulk_create(batch)
                    batch = []
            cls.objects.bulk_create(batch)

