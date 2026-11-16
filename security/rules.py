XSS_PATTERNS = [
    r"<script.*?>.*?</script>",
    r"alert\s*\(",
]

SQLI_PATTERNS = [
    r"or\s+1=1",
    r"union\s+select",
    r"--",
]