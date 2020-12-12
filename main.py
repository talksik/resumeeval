import pdfreader
import textdistance
from pdfreader import PDFDocument, SimplePDFViewer

# Preparing resume parsing
file_name = "example_resume.pdf"
fd = open(file_name, "rb")
doc = SimplePDFViewer(fd)
doc.render()

# Getting the string content from the file
resume_content_dump = " ".join(doc.canvas.strings)
sucky_resume_content = " ".join(doc.canvas.strings[:5])
# print(resume_content_dump)

# Example inputs from the company
previous_roles = ["technical product manager", "product manager"]
previous_skills = ["react", "sql"]
previous_roles.extend(previous_skills)
client_interests = previous_roles
print(client_interests)

# Test of text distance algo
print(textdistance.levenshtein.normalized_similarity('ass', 'a s s'))

# Finding total final score for words
list_norm_scores = [textdistance.jaro_winkler(resume_content_dump, word) for word in client_interests]
avg_normalized_score = sum(list_norm_scores) / len(list_norm_scores)

# sucky resume
sucky_list_norm_scores = [textdistance.jaro_winkler(sucky_resume_content, word) for word in client_interests]
sucky_avg_normalized_score = sum(sucky_list_norm_scores) / len(sucky_list_norm_scores)

print('stud resume: ', avg_normalized_score * 100)
print('sucky: ', sucky_avg_normalized_score * 100)
