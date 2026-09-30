// Workshop 5: Tag Generator
function generateHtmlTag(tag, text) {
    return `<${tag}>${text}</${tag}>`;
}
console.log(generateHtmlTag("h1", "JavaScript Certification"));