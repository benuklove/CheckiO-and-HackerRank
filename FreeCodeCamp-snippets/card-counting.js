var count = 0;

function cc(card) {
  // Only change code below this line
  var status = "";
  if (typeof card === 'number') {
    if (card > 1 && card < 7) {
      count++;
    }
  }
  switch (card) {
    case 10:
    case "J":
    case "Q":
    case "K":
    case "A":
      count--;
  }
  if (count > 0) {
    status = count + " Bet";
  }
  else {
    status = count + " Hold";
  }
  return status;
  // Only change code above this line
}

// Add/remove calls to test your function.
// Note: Only the last will display
cc(2); cc(3); cc(7); cc('K'); cc('A');
