var casper = require('casper').create({
    verbose: true,
    logLevel: "debug",
    stepTimeout: 60000,
    pageSettings:{
        loadImages:  false
    }
});

var depCode = casper.cli.get(0)
var depAirport = casper.cli.get(1)
var arrCode = casper.cli.get(2)
var arrAirport = casper.cli.get(3)
var queryDate = casper.cli.get(4)

var fs = require('fs');

var queryUrl = "http://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=" + depAirport + "&searchArrivalAirport=" + arrAirport + "&searchDepartureTime=" + queryDate + "&startSearch=true&fromCode=" + depCode + "&toCode=" + arrCode + "&from=qunarindex&lowestPrice=null"

casper.echo("URL: " + queryUrl)

casper.on('page.resource.requested', function(requestData, request) {
    if (requestData.url.indexOf('dis.cn.criteo.com') > 0) {
        request.abort();
    }
});

casper.start(queryUrl)

//casper.waitForSelectorTextChange('div#hdivResultPanel', function() {
casper.waitWhileSelector('.loading', function() {
    //this.echo(this.getPageContent())
    fs.write('/tmp/debug.html', this.getPageContent(), 'w')
}, function() {
    console.log('Timeout')
}, 60000);

casper.run();
