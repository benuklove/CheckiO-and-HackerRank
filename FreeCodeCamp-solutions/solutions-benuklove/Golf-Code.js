
function golfScore(par, strokes) {
  // Only change code below this line
  var results = ["Hole-in-one!", "Eagle", "Birdie", "Par", "Bogey",
                "Double Bogey", "Go Home!"];
  var result;
  var diff = strokes - par;
  if (strokes == 1) {
    result = results[0];
  }
  else if (diff <= -2) {
    result = results[1];
  }
  else if (diff <= -1) {
    result = results[2];
  }
  else if (diff >= 3) {
    result = results[6];
  }
  else if (diff >= 2) {
    result = results[5];
  }
  else if (diff >= 1) {
    result = results[4];
  }
  else {
    result = results[3];
  }
  
  return result;
  // Only change code above this line
}

// Change these values to test
golfScore(5, 4);
