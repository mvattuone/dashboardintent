$ = require('jquery');
d3 = require('d3');
nvd3 = require('nvd3');
randomColor = require('randomcolor');

window.app = {}

app.initialize = function() {

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = $.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    function loadTrends() {

        window.data = $('#trends').data('trends');

        nvd3.addGraph(function(){

            var data = $('#trends').data('trends'),
                chartContainer = $('<div />')[0],
                svg = $('<svg style="height:200px;width:100%;" />')[0],
                chart = nvd3.models.pieChart();

            $(chartContainer).append(svg);

            $('#trends').append(chartContainer);

            chart.x(function(d) { return d.label })
                 .y(function(d) { return d.value })
                 .labelType("percent")
                 .donut(true)


            d3.select(svg).datum(data).call(chart);
            nv.utils.windowResize(
                function() {
                    chart.update();
                }
            );
        });

    }

    function buildChart(data) {
        // for each group in currentGroups
        // take the metrics associated with it
        // and build a chart, then append to DOM



         nvd3.addGraph(function(){
            var chart = nvd3.models.multiBarChart(),
                chartContainer = $('<div class="chart col col-12" />')[0],
                svg = $('<svg style="height:100%;width:100%;" />')[0];

            $(chartContainer).append(svg);

            $('#charts').append(chartContainer);
            d3.select(svg).datum(data).call(chart);

            nv.utils.windowResize(
                function() {
                    chart.update();
                }
            );


        });

    }

    function updateDashboard(data) {
        colors = randomColor({
            count: data.length
        });

        var newData = [];

        data.forEach(function(d) {
            var group = d.shift(),
                metrics = [];

                d.forEach(function(metric, i) {
                    var label;
                    switch (i) {
                        case 0:
                            label = "Lowest"
                            break;
                        case 1:
                            label = "Lower"
                            break;
                        case 2:
                            label = "Neutral"
                            break;
                        case 3:
                            label = "Higher"
                            break;
                        case 4:
                            label = "Highest"
                            break;
                        default:
                            label = "Not gonna happen"
                            break;
                    }

                    metrics.push({ 'x': label, 'y': metric });
                });

            var template = "<div class='controls-group'><label>" + group + "</label></div>";
            var dataSet = {
                'key': group,
                'values': metrics,
                'color': colors.shift()
            };

            console.log(newData);

            newData.push(dataSet);
            $('#groups').append(template);
        });

        buildChart(newData);
    }

    function toggleView() {
        var data = {
            'metricName': $('#metric').val()
        }

        $.ajax({
            method: 'POST',
            url: '/get-groups/',
            data: data,
            dataType: 'json',
        }).then(function(data) {
            updateDashboard(data);
        }).fail(function(error) {
            throw new Error(error.responseText);
        });
    }

    function clearDashboard() {
        $('.chart').remove();
        $('.controls-group').remove();
        return this;
    }

    $('#metric').on('change', function(e) {
        e.preventDefault();
        clearDashboard();
        toggleView();
    });

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $(document).ready(function() {

        loadTrends();
        toggleView();

    });
}

$(function() {


    app.initialize();




});
