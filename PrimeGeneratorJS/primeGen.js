
function nextPrime(){

var primeCheck = parseInt(document.getElementById('currentPrime').value, 10);
var factorCheck = primeCheck;
var noPrime = true;
var previousPrime = document.getElementById('previousPrime').innerHTML;

while(noPrime){
  factorCheck -= 1;

  if(factorCheck == 1){
    noPrime = false;
    document.getElementById('currentPrime').value = primeCheck + 2;
    document.getElementById('primebox').innerHTML = primeCheck;
    document.getElementById('previousPrime').innerHTML = primeCheck +  "<br>" + previousPrime;
    }

  if(primeCheck % factorCheck == 0){
    primeCheck += 2;
    factorCheck = primeCheck;
  }

}
}
