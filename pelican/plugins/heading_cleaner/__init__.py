# import re
# import logging
# from pelican import signals

# logger = logging.getLogger(__name__)

# def clean_headings(path, context):
#     if 'content' not in context:
#         logger.warning(f"No content found in context for {path}")
#         return

#     original_content = context['content']
    
#     # Remove all h1 headings
#     modified_content = re.sub(r'<h1>.*?</h1>', '', original_content, flags=re.DOTALL)
    
#     # Remove h2 and h3 headings that are "Introduction" or "Conclusion"
#     modified_content = re.sub(r'<h[23]>\s*(Introduction|Conclusion)\s*</h[23]>', '', modified_content, flags=re.IGNORECASE)
    
#     # Remove any resulting empty paragraphs
#     modified_content = re.sub(r'<p>\s*</p>', '', modified_content)

#     if original_content != modified_content:
#         context['content'] = modified_content
#         logger.info(f"Headings cleaned in {path}")
#     else:
#         logger.info(f"No changes made to {path}")

# def register():
#     logger.info("Registering heading_cleaner plugin")
#     signals.content_written.connect(clean_headings)
#     logger.info("heading_cleaner plugin registered successfully")