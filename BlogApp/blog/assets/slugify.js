const title = document.querySelector('input[name=title]');
const slug = document.querySelector('input[name=slug]');
slug.readOnly = true;

title.addEventListener("keyup",(evnt)=>{
    slug.value = slugify(title.value);
})

const slugify = (val)=>{
    return val.toString().toLowerCase().trim()
    .replace(/&/g,'-and-')    //replace & with and
    .replace(/[\s\W-]+/g,'-')  //replace spaces, non-word chars and dashes with a single dash
}