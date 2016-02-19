import re

resume = '''IRMA PARKER 
Phone: 763-555-5555 
Email: jobhunter@success.com

OBJECTIVE: Registered Medical Laboratory Technician requiring extensive experience with success in pediatrics and at a trauma emergency hospital.

SUMMARY OF SKILLS AND EXPERIENCE 654-234-5555

LAB TECHNICIAN-- Highly skilled lab technologist with experience serving ER, Urgent Care, Pediatric ER, and Stab-Room Trauma Unit.  Processed cultures in microbiology, gram stains, urinalysis and various manual tests.

PHLEMBOTOMY-- Inpatient and outpatient, pre-op and post-op, blood draws.  Recognized for exceptional skill in serving hard-to-draw patients and children.

INSTRUMENT MAINTENANCE-- Skilled in troubleshooting and maintenance of technical equipment.

TEACHING-- Responsible for training staff on equipment operation and procedures.

QUALITY CONTROL—Maintained high quality standards with an emphasis on accuracy.  Maximized performance through organization, equipment testing, and procedures development.

EMPLOYMENT HISTORY

MEDICAL LABORATORY TECHNICIAN, ASCP 
May 1995 to September 2006 Hennepin County Medical Center 
*Increased lab efficiency through improved processing procedures, development of technical equipment, lab layout, and design. 
*Maintained peak lab performance.  Blood samples from Stab-Room Trauma Unit had to be accurately processed within two minutes! 
*Assisted medical staff in the research and development of “Kiss of Life” mask used in respiratory emergency care.

PHLEBOTOMIST 
August 1989 to March 1995 Minneapolis Children’s Medical Center

EDUCATION

CERTIFIED: American Society of Clinical Pathologists 
MEDICAL LABORATORY TECHNICIAN (GPA 3.5) 
College of St. Catherine 1987 
BIOLOGY/CHEMISTRY (117 credits) 
Mankato State University 1985

'''

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume))

