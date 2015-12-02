$ = require('jquery');
d3 = require('d3');
nvd3 = require('nvd3');

window.app = {}

app.initialize = function() { 

    function buildTrend() {
        // TBD
    }


    function buildChart(data) {
        // for each group in currentGroups
        // take the metrics associated with it
        // and build a chart, then append to DOM

         nvd3.addGraph(function(){
            var chart = nvd3.models.lineChart();
            var svg = $('<svg style="height:250px" />')[0];

            $("#charts > div").append(svg);

            d3.select(svg).datum(data).call(chart);
            chart.pointSize(0);
            nv.utils.windowResize(
                function() {
                    chart.update();
                }
            );
            
        });

    }

    function buildGroups() {
        app.currentGroups.forEach(function(group) {
            var template = "<li class='panel bg-navy'>" + group.name + "</li>";
            var data = [{
                'key': group.name,
                'values': group.metrics,
                'color': '#222'
            }]

            $('#pages > div').append(template);
            buildChart(data);
            
        })
        // for each group in currentGroups
        // take the group that was built
        // and populate a template that 
        // we then append to the DOM
        // probably too simple to warrant 
        // a real template, just
        // append html $('foo').html()
    }

    function toggleView() {
        var data = {
            'metric': $('#metrics').val()
        }

        $.ajax({
            method: 'POST',
            url: 'retrieve/',
            data: data,
            dataType: 'json',
            success: function(data, jqXhr) {
                app.currentGroups = data;
            },
            error: function(error) {
                // does this even work
                throw new Error(error);
            }
        }).then(function() {
            buildGroups();
        });
    }

    $('#metrics').on('change', function() {
        $('#pages > div').empty();
        $('#charts > div').empty();
        toggleView();
    });

    toggleView();
}

$(function() {


    app.initialize();




});

