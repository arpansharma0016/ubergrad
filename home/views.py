from django.shortcuts import render
from django.http import JsonResponse
import json


def index(request):
    return render(request, "index.html")

def first(request):
    return JsonResponse({'one': 'MASTER IN COMPUTER SCIENCE IN US', 'two': 'Grow your skills to Advance <br> Your Career Path'})

def second(request):
    return JsonResponse({'one': "Computer Science is the study of processes to develop mathematical models that bridge human interaction with computers by writing programs for software, application or a website. In this age of computers and technology and given the filed's broad range and flexibility, It has become one of the most preferred courses in the world.<br><br> With Computer Science being the most popular course, Masters in Computer Science in the USA is naturally one of the preferred choices for aspiring Indian students. The US is the home to some of the top notch companies like Microsoft, IM, Google and many others, and this provides Computer Science graduates in the US with innumerable job options in this field.<br><br> Here you will be finding all the details you will need to pursue your MS in Computer Science in the USA."})

def third(request):
    li = ['Artificial Intelligence', 'Big Data', 'Cloud Computing', 'Computer Architecture', 'Computer Graphics', 'Computer Networks',
    'Cyber Security', 'Data Structures', 'Embedded Systems', 'Information Management and Data Analytics', 'Machine Learning', 'Mobile and Web Computing', 'Software Engineering']

    return JsonResponse({'one':li})

def fourth(request):
    li = [
        ['Degree', "A four years Bachelor's degree in a related field from an accredited institution with a minimum of 65%"],
        ['IELTS', "A minimum score of 6.5"],
        ['TOEFL iBT', "Acceptable Overall Score Range: 79-100"],
        ['General GRE', "A minimum of 300 is required to get into a reasonably good University. Top Universities like Stanford require close to 330 range."],
        ['Statement of Purpose (SOP)', "2 SOPs"],
        ['Letter of Recommendation (LOR)', "Three letters of recommendation (including atleast two academic references)"]
    ]

    return JsonResponse({'one':li})

def fifth(request):
    li = [
        ['Stanford University', '1', "$55,890", "(approx 40.24 lakhs INR)"],
        ['Massachusetts Intitute of Technology', '2', "$43,210", "(approx 31.11 lakhs INR)"],
        ['Carnegie Melon University', '3', "$98,000", "(approx 70.56 lakhs INR)"],
        ['Harward University', '4', "$43,296", "(approx 31.17 lakhs INR)"],
        ['Princeton University', '5', "$1,07,540", "(approx 77.42 lakhs INR)"],
        ['California Institute of Technology', '6', "$41,408", "(approx 29.81 lakhs INR)"],
        ['University of California, Los Angeles', '7', "$63,898", "(approx 46 lakhs INR)"],
        ['Cornelle University', '8', "$59,000", "(approx 42.48 lakhs INR)"],
        ['Georgia Institute of Technology', '9', "$62,740", "(approx 45.17 lakhs INR)"],
        ['Columbia University', '10', "$63,120", "(approx 45.44 lakhs INR)"]
    ]

    return JsonResponse({'one': li})

def sixth(request):
    li = [
        'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/603px-Amazon_logo.svg.png',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Deloitte.svg/800px-Deloitte.svg.png',
        'https://upload.wikimedia.org/wikipedia/en/thumb/d/d7/Logo_of_Common_Service_Centres.svg/220px-Logo_of_Common_Service_Centres.svg.png',
        'https://blogs.microsoft.com/wp-content/uploads/prod/2012/08/8867.Microsoft_5F00_Logo_2D00_for_2D00_screen-1920x706.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/HP_logo_2012.svg/100px-HP_logo_2012.svg.png',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/488px-Apple_logo_black.svg.png',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/368px-Google_2015_logo.svg.png',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Facebook_Logo_%282019%29.png/600px-Facebook_Logo_%282019%29.png',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Intel_logo_%282006-2020%29.svg/800px-Intel_logo_%282006-2020%29.svg.png'
    ]

    return JsonResponse({'one': li})

def seventh(request):
    one = "With Computer Science being one of the courses among STEM fields, graduates have the opportunity to gain work experience of up to 36 months in the USA. As a computer science graduate in the USA, you will have a vast range of career opportunities from something as unique as a game developer to as common aas a software developer or IT manager. Below are some of the popular job designations you can find yourself in after completing an MS in Computer Science in the USA."
    two = [
        'Application Developer',
        'Data Analyst',
        'Database Administrator',
        'Forensic Computer Analyst',
        'Game Designer',
        'Game Developer',
        'IT Consultant',
        'Multimedia Programmer',
        'Software Engineer',
        'UX Designer',
        'VFX Artist',
        'Web Designer',
        'Web Developer'
    ]
    three = "Students who have completed their MS in Computer Science in the USA can find jobs with median salaries of $100,000 per year (approx 75 lakhs INR)."
    four = "To conclude, doing MS in Computer Science in the USA is one of the best career to pursue given its current demand for skilled people in this field and its future prediction of demands in many sectors. We believe the above information will help you in making up your mind in pursuing it. If you require any assistance in finding and applying to universities, you can always contact our Student Support Team."

    return JsonResponse({'one': one, 'two': two, 'three': three, 'four': four})

def eighth(request):
    one = "Ubergrad.com is a study abroad website that helps students to APPLY and ENROLL at top Universities overseas, all at no cost to them. 'Uber' = super (in German), 'grad' = graduate<br><br> Student Support Office : #207, 2nd Floor, Manjeera Majestic Commercial, jNTU Hi-Tech City Road, KPHB, Hyderabad, Telangana - 500072, India."
    two = [
        "About Us",
        "Success Stories",
        "Terms & Conditions",
        "Privacy Policy",
        "Disclaimer"
    ]
    three = [
        "Countries",
        "Universities",
        "Courses",
        "Exams",
        "Talk to Our Counsellor"
    ]
    four = [
        "Why Study in USA",
        "Why Study in UK",
        "Why Study in Canada",
        "Why Study in New Zealand",
        "Why Study in Ireland"
    ]

    return JsonResponse({'one': one, 'two': two, 'three': three, 'four': four})