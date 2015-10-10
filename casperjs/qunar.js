var casper = require('casper').create({
    verbose: true,
    logLevel: 'debug'
})

var fs = require('fs');

casper.start('http://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E5%8D%97%E4%BA%AC&searchArrivalAirport=%E5%A4%A7%E8%BF%9E&searchDepartureTime=2015-10-12&searchArrivalTime=2015-10-15&nextNDays=0&startSearch=true&fromCode=NKG&toCode=DLC&from=qunarindex&lowestPrice=null');

casper.waitWhileSelector('.loading', function() {
    this.echo('.selector is no more!');
    this.echo(this.getPageContent())
});

casper.run();
