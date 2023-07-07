// check button click for filtering top, then run python function
$(function() {
    $('a#top').on('click', function(e) {
      e.preventDefault()

      // setting colors for all buttons
      //top
      document.getElementById("button_top").style.background = "#FF5700";
      document.getElementById("button_top").style.color = "white";
      
      // hot 
      document.getElementById("button_hot").style.background = "#ececec";
      document.getElementById("button_hot").style.color = "black";

      // new
      document.getElementById("button_new").style.background = "#ececec";
      document.getElementById("button_new").style.color = "black";

      // rising
      document.getElementById("button_rising").style.background = "#ececec";
      document.getElementById("button_rising").style.color = "black";
      
      $.getJSON('/filter/top',
           {
        // do nothing
      });
      
      return false;
    });
  });

// check button click for filtering hot, then run python function
$(function() {
    $('a#hot').on('click', function(e) {
      e.preventDefault()

      // setting colors for all buttons
      //top
      document.getElementById("button_top").style.background = "#ececec";
      document.getElementById("button_top").style.color = "black";
      
      // hot 
      document.getElementById("button_hot").style.background = "#FF5700";
      document.getElementById("button_hot").style.color = "white";

      // new
      document.getElementById("button_new").style.background = "#ececec";
      document.getElementById("button_new").style.color = "black";

      // rising
      document.getElementById("button_rising").style.background = "#ececec";
      document.getElementById("button_rising").style.color = "black";
      
      $.getJSON('/filter/hot',
           {
        //do nothing
      });
      return false;
    });
  });

// check button click for filtering new, then run python function
$(function() {
    $('a#new').on('click', function(e) {
      e.preventDefault()

      // setting colors for all buttons
      //top
      document.getElementById("button_top").style.background = "#ececec";
      document.getElementById("button_top").style.color = "black";
      
      // hot 
      document.getElementById("button_hot").style.background = "#ececec";
      document.getElementById("button_hot").style.color = "black";

      // new
      document.getElementById("button_new").style.background = "#FF5700";
      document.getElementById("button_new").style.color = "white";

      // rising
      document.getElementById("button_rising").style.background = "#ececec";
      document.getElementById("button_rising").style.color = "black";
      

      $.getJSON('/filter/new',
           {
        //do nothing
      });
      return false;
    });
  });

  // check button click for filtering rising, then run python function
$(function() {
    $('a#rising').on('click', function(e) {
      e.preventDefault()

      // setting colors for all buttons
      //top
      document.getElementById("button_top").style.background = "#ececec";
      document.getElementById("button_top").style.color = "black";
      
      // hot 
      document.getElementById("button_hot").style.background = "#ececec";
      document.getElementById("button_hot").style.color = "black";

      // new
      document.getElementById("button_new").style.background = "#ececec";
      document.getElementById("button_new").style.color = "black";

      // rising
      document.getElementById("button_rising").style.background = "#FF5700";
      document.getElementById("button_rising").style.color = "white";
      

      $.getJSON('/filter/rising',
           {
        //do nothing
      });
      return false;
    });
  });


// check submit button click
const theButton = document.querySelector("#submit_button");

theButton.addEventListener("click", () => {
    theButton.classList.add("button--loading");
});