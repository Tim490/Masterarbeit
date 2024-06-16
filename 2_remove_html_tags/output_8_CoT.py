import re

def remove_html_tags(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    if not s:
        return ""
    
    tag_pattern = re.compile(r'<[^>]+>')
    comment_pattern = re.compile(r'<!--.*?-->', re.DOTALL)
    doctype_pattern = re.compile(r'<!DOCTYPE[^>]+>', re.IGNORECASE)
    
    # Remove comments
    s = re.sub(comment_pattern, '', s)
    # Remove doctype declarations
    s = re.sub(doctype_pattern, '', s)
    # Remove HTML tags
    s = re.sub(tag_pattern, '', s)
    
    return s.strip()