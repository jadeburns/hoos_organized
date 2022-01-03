# Generated by Django 3.2.7 on 2021-12-04 21:03

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('credits', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)])),
                ('code', models.CharField(choices=[('ACCT', 'Accounting'), ('AE', 'Aerospace Engineering'), ('AAS', 'African American and African Studies'), ('AIRS', 'Air Science'), ('AMST', 'American Studies'), ('ANTH', 'Anthropology'), ('APST', 'Applied Statistics'), ('APMA', 'Applied Mathematics'), ('ARAB', 'Arabic'), ('ARCH', 'Architecture'), ('ARCY', 'Archaeology'), ('ARH', 'Architectural History'), ('ARTH', 'Art History'), ('ARAD', 'Arts Administration'), ('ASL', 'American Sign Language'), ('ASTR', 'Astronomy'), ('BIOL', 'Biology'), ('BME', 'Biomedical Engineering'), ('CHEM', 'Chemistry'), ('CHE', 'Chemical Engineering'), ('CHIN', 'Chinese'), ('CHTR', 'Chinese in Translation'), ('CE', 'Civil Engineering'), ('CLAS', 'Classics'), ('COGS', 'Cognitive Science'), ('COMM', 'Commerce'), ('CPLT', 'Comparative Literature'), ('CPE', 'Computer Engineering'), ('CS', 'Computer Science'), ('CREO', 'Creole'), ('DANC', 'Dance'), ('DRAM', 'Drama'), ('DS', 'Data Science'), ('EALC', 'East Asian Languages, Literatures, and Cultures'), ('ECED', 'Early Childhood Education'), ('ECE', 'Electrical and Computer Engineering'), ('ECON', 'Economics'), ('EDHS', 'Education-Human Services'), ('EDLF', 'Education-Leadership, Foundations, and Policy'), ('EGMT', 'Engagement'), ('EE', 'Electrical Engineering'), ('ELED', 'Elementary Education'), ('ENCW', 'Creative Writing'), ('ENGL', 'English'), ('ENGR', 'Engineering'), ('ESCI', 'Engineering Science'), ('ENTP', 'Entrepreneurship'), ('EVSC', 'Environmental Sciences'), ('ETP', 'Environmental Thought and Practice'), ('ENWR', 'Writing and Rhetoric'), ('ESL', 'English as a Second Lanaguge'), ('EVAT', 'Environmental Sciences-Atmospheric Sciences'), ('EVEC', 'Environmental Sciences-Ecology'), ('EVGE', 'Environmental Sciences-Geosciences'), ('EVHY', 'Environmental Sciences-Hydrolgy'), ('EAST', 'East Asian Languages, Literatures, and Culture'), ('FREN', 'French'), ('FRTR', 'French in Translation'), ('GDS', 'Global Development Studies'), ('GERM', 'German'), ('GEST', 'German Studies'), ('GETR', 'German in Translation'), ('GLST', 'Global Studies'), ('GREE', 'Greek'), ('GSDS', 'Global Studies-Global Studies'), ('GSSJ', 'Global Studies-Security and Justice'), ('GSVS', 'Global Studies-Environments and Sustainability'), ('HEBR', 'Hebrew'), ('HIND', 'Hindi'), ('HIST', 'History'), ('HIAF', 'History-African History'), ('HIEA', 'History-East Asian History'), ('HIEU', 'History-European History'), ('HILA', 'History-Latin American History'), ('HIME', 'History-Middle Eastern History'), ('HISA', 'History-South Asian History'), ('HIUS', 'History-United States History'), ('HBIO', 'Human Biology'), ('INST', 'Interdisciplinary Studies'), ('BIS', 'Interdisciplinary Studies'), ('ITAL', 'Italian'), ('ITTR', 'Italian in Translation'), ('JAPN', 'Japanese'), ('JWST', 'Jewish Studies'), ('JPTR', 'Japanese in Translation'), ('KICH', 'Maya Kiche'), ('KINE', 'Kinesiology'), ('KOR', 'Korean'), ('LATI', 'Latin'), ('LAST', 'Latin American Studies'), ('LING', 'Linguistics'), ('MAE', 'Mechanical & Aerospace Engineering'), ('MATH', 'Mathematics'), ('MSE', 'Materials Science and Engineering'), ('ME', 'Mechanical Engineering'), ('MDST', 'Media Studies'), ('MSP', 'Medieval Studies'), ('MEST', 'Middle Eastern Studies'), ('MUSI', 'Music'), ('MUBD', 'Music-Marching Band'), ('MUEN', 'Music-Ensembles'), ('MUPF', 'Music-Private Performance Instruction'), ('MESA', 'Middle Eastern and South Asian Languages and Cultures'), ('NEUR', 'Neuroscience'), ('NUCO', 'Nursing Core'), ('NURS', 'Nursing'), ('PERS', 'Persian'), ('PETR', 'Persian in Translation'), ('PHIL', 'Philosophy'), ('PHS', 'Public Health Sciences'), ('PHS', 'Public Health Sciences'), ('PHYS', 'Physics'), ('PLAD', 'Politics-Departmental Seminar'), ('PLAP', 'Politics-American Politics'), ('PLCP', 'Politics-Comparative Politics'), ('PLIR', 'Politics-International Relations'), ('PLPT', 'Politics-Political Theory'), ('POL', 'Polish'), ('POLI', 'Politics'), ('PPL', 'Political Philosophy, Policy, and Law'), ('PST', 'Political and Social Thought'), ('PORT', 'Portuguese'), ('BPHM', 'Professional Studies in Health Sciences Management'), ('PSYC', 'Psychology'), ('RELG', 'Religious Studies'), ('RELA', 'Religion-African Religions'), ('RELB', 'Religion-Buddhism'), ('RELC', 'Religion-Christianity'), ('RELH', 'Religion-Hinduism'), ('RELI', 'Religion-Islam'), ('RELJ', 'Religion-Judaism'), ('RUSS', 'Russian'), ('RUTR', 'Russian in Translation'), ('SANS', 'Sanskrit'), ('SAST', 'South Asian Studies'), ('SLAV', 'Slavic Languages and Literatures'), ('SLFK', 'Slavic Folklore & Oral Literature'), ('SOC', 'Sociology'), ('SPAN', 'Spanish'), ('EDIS', 'Special Education'), ('SCDI', 'Speech Communication Disorders'), ('STAT', 'Statistics'), ('STS', 'Science, Technology, and Society'), ('ARTS', 'Studio Art'), ('SWAH', 'Swahili'), ('SYS', 'Systems Engineering'), ('PLAN', 'Urban and Environmental Planning'), ('URDU', 'Urdu'), ('USEM', 'University Seminar'), ('WGS', 'Women, Gender, & Sexuality'), ('YSIN', 'Youth & Social Innovation')], max_length=4)),
                ('courseNumber', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Course Number')),
                ('year', models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(2000)])),
                ('professor', models.CharField(default='Staff', max_length=200)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dueDate', models.DateTimeField(default=datetime.datetime(2021, 12, 4, 21, 33, 48, 233751, tzinfo=utc))),
                ('remindTime', models.IntegerField(choices=[(10, '10 min'), (15, '15 min'), (30, '30 min'), (45, '45 min'), (60, '1 hour'), (75, '1 hour 15 min'), (90, '1 hour 30 min'), (120, '2 hours'), (180, '3 hours'), (240, '4 hours'), (300, '5 hours'), (360, '6 hours'), (420, '7 hours'), (480, '8 hours'), (540, '9 hours'), (600, '10 hours'), (660, '11 hours'), (720, '12 hours'), (960, '16 hours'), (1200, '20 hours'), (1440, '1 day'), (2880, '2 days'), (4320, '3 days'), (5760, '4 days'), (7200, '5 days'), (8640, '6 days'), (10080, '1 week')], default=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('dueDate',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computingID', models.CharField(max_length=10, verbose_name='Computing ID')),
                ('major', models.CharField(blank=True, choices=[('AE', 'Aerospace Engineering'), ('AAS', 'African American and African Studies'), ('AMST', 'American Studies'), ('ANTH', 'Anthropology'), ('APST', 'Applied Statistics'), ('ARCY', 'Archaeology'), ('ARH', 'Architectural History'), ('ARCH', 'Architecture'), ('ASTR', 'Astronomy'), ('ASTROPHYS', 'Astronomy-Physics'), ('BIS', 'Interdisciplinary Studies'), ('BPHM', 'Professional Studies in Health Sciences Management'), ('BIOL', 'Biology'), ('BME', 'Biomedical Engineering'), ('CHEM', 'Chemistry'), ('CHE', 'Chemical Engineering'), ('CE', 'Civil Engineering'), ('CLAS', 'Classics'), ('COGS', 'Cognitive Science'), ('COMM', 'Commerce'), ('CPLT', 'Comparative Literature'), ('CPE', 'Computer Engineering'), ('BACS', 'Computer Science, BA'), ('BSCS', 'Computer Science, BS'), ('DRAM', 'Drama'), ('ECED', 'Early Childhood Education'), ('EAST', 'East Asian Studies'), ('ECON', 'Economics'), ('EE', 'Electrical Engineering'), ('ELED', 'Elementary Education'), ('ESCI', 'Engineering Science'), ('ENGL', 'English'), ('EVSC', 'Environmental Sciences'), ('ETP', 'Environmental Thought and Practice'), ('TEACH', 'Five-Year Teacher Education Program'), ('FREN', 'French'), ('GERM', 'German'), ('GEST', 'German Studies'), ('GLST', 'Global Studies'), ('HIST', 'History'), ('ARTH', 'History of Art'), ('HBIO', 'Human Biology'), ('JWST', 'Jewish Studies'), ('KINE', 'Kinesiology'), ('LAST', 'Latin American Studies'), ('LING', 'Linguistics'), ('MSE', 'Materials Science and Engineering'), ('MATH', 'Mathematics'), ('ME', 'Mechanical Engineering'), ('MDST', 'Media Studies'), ('MSP', 'Medieval Studies'), ('MESA', 'Middle Eastern and South Asian Languages and Cultures'), ('MUSI', 'Music'), ('NEUR', 'Neuroscience'), ('NURS', 'Nursing'), ('PHIL', 'Philosophy'), ('PHYS', 'Physics'), ('PST', 'Political and Social Thought'), ('PPL', 'Political Philosophy, Policy, and Law'), ('POLI', 'Politics'), ('PSYC', 'Psychology'), ('RELG', 'Religious Studies'), ('SLAV', 'Slavic Languages and Literatures'), ('SOC', 'Sociology'), ('SPAN', 'Spanish'), ('EDIS', 'Special Education'), ('SCDI', 'Speech Communication Disorders'), ('STAT', 'Statistics'), ('ARTS', 'Studio Art'), ('SYS', 'Systems Engineering'), ('PLAN', 'Urban and Environmental Planning'), ('WGS', 'Women, Gender, & Sexuality'), ('YSIN', 'Youth & Social Innovation'), ('____', 'Undeclared')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='notes/')),
                ('isVisible', models.BooleanField(default=True)),
                ('theClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.classes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='classes',
            constraint=models.UniqueConstraint(fields=('code', 'courseNumber', 'professor', 'year'), name='unique-class'),
        ),
    ]
