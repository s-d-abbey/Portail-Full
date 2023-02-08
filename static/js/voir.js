
    var week_toggle = document.getElementById("week-toggle")
    var day_toggle = document.getElementById("day-toggle")
    var week_content = document.querySelector(".week-content")
    var day_content = document.querySelector(".day-content")
    week_toggle.addEventListener('click', () =>{
            week_toggle.classList.add('active')
            day_toggle.classList.remove('active')
            week_content.classList.remove('inactive')
            day_content.classList.remove("active")

        })
    day_toggle.addEventListener('click', () =>{
            day_toggle.classList.add('active')
            week_toggle.classList.remove('active')
            week_content.classList.add("inactive")
            day_content.classList.add("active")
        })