$(document).ready() {
  console.log('testing');
}


document.querySelector('#stock-refresher').onclick = function() {
  refreshQuotes()
}

function refreshQuotes() {
  console.log(quotes_api);
  var request = new XMLHttpRequest();
  request.open('GET', quotes_api, true);
  request.onload = function(){ 
    if (request.status >= 200 && request.status < 400) {
      // Success!
      var data = JSON.parse(request.responseText);
      renderQuotes(shuffle(data))
    } else {
      // We reached our target server, but it returned an error
    }
  };
  request.onerror = function() {
    // There was a connection error of some sort
  };
  request.send();
}

function renderQuotes(quotes) {
  var quote = quotes[0]
  var quoteBlock = document.querySelector('#quote-template')
  document.querySelector('#quotes').innerHTML = ""
  createSingleQuote(quoteBlock, quotes.slice(0,3))
}

function createSingleQuote(template, quotes) {
  originalTemplate = template
  quotes.forEach(function(quote){
    template = originalTemplate
  
    var isPositive = quote['Change']['Amount'] > 0
    var isNegative = quote['Change']['Amount'] < 0
    template.querySelector('img.company-image').src = `https://g.foolcdn.com/art/companylogos/mark/${quote['Symbol']}.png`
    template.querySelector('h3.company-name').innerText = quote['CompanyName']
    template.querySelector('span.market').innerText = quote['ExchangeName']
    template.querySelector('span.symbol').innerText = quote['Symbol']
    template.querySelector('h4.current-price').innerText = `$${quote['CurrentPrice']['Amount'].toFixed(2)}`
    template.querySelector('h4.price-change-amount').innerText = `$${quote['Change']['Amount'].toFixed(2)}`
    template.querySelector('h4.price-change-amount').classList.toggle("price-pos", isPositive)
    template.querySelector('h4.price-change-amount').classList.toggle("price-neg", isNegative)
    template.querySelector('h4.price-change-percent').innerText = `${Math.floor(quote['PercentChange']['Value'] * 10000) / 1000}%`
    var clone = document.importNode(template, true);  
    document.querySelector("#quotes").prepend(clone);  
    // document.querySelector('#quotes').append(template)
  })
}

function shuffle(array) {
  return array.sort(() => Math.random() - 0.5);
}