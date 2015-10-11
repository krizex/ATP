var casper = require('casper').create({
    pageSettings:{
        loadImages:  false
    }
});


var queryDate = casper.cli.get(0)

var fs = require('fs');

var queryUrl = "http://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E5%8D%97%E4%BA%AC&searchArrivalAirport=%E5%A4%A7%E8%BF%9E&searchDepartureTime=" + queryDate + "&startSearch=true&fromCode=NKG&toCode=DLC&from=qunarindex&lowestPrice=null"

casper.echo(queryUrl)

casper.start(queryUrl)

casper.waitWhileSelector('.loading', function() {
    //this.echo(this.getPageContent())
    fs.write('searchResult.html', this.getPageContent(), 'w')
});

casper.run();
