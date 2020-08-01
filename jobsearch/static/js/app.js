const jobBtns = Array.from(document.getElementsByClassName('btn-shortlist'))
const shortlistBtns = Array.from(document.getElementsByClassName('btn-shortlisted'))
console.log(jobBtns)

jobBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        let jobId = this.dataset.jobid
        let shortlistBtn = document.getElementById(jobId)
        console.log(shortlistBtn)
        shortlistBtn.style.display = 'inline-block'
        btn.style.display = 'none'
    });
});
