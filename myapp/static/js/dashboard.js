$(document).ready(function() {
    var apiUrl = '/api/insights/';

    // Fetch data on page load with empty filters
    fetchFilteredInsights({});

    // Function to fetch data from API based on filters
    function fetchFilteredInsights(filters) {
        $.ajax({
            url: apiUrl,
            type: 'GET',
            data: filters,
            dataType: 'json',
            success: function(data) {
                renderCharts(data);
                populateFilters(data);
            },
            error: function(error) {
                console.log('Error fetching data:', error);
            }
        });
    }

    // Function to populate filter options dynamically
    function populateFilters(data) {
        var endYearFilter = $('#endYearFilter');
        var topicFilter = $('#topicFilter');
        var sectorFilter = $('#sectorFilter');
        var regionFilter = $('#regionFilter');

        // Clear previous options
        endYearFilter.empty().append('<option value="">All</option>');
        topicFilter.empty().append('<option value="">All</option>');
        sectorFilter.empty().append('<option value="">All</option>');
        regionFilter.empty().append('<option value="">All</option>');

        // Extract unique values for each filter
        var endYears = getUniqueFieldValues('end_year', data);
        var topics = getUniqueFieldValues('topic', data);
        var sectors = getUniqueFieldValues('sector', data);
        var regions = getUniqueFieldValues('region', data);

        // Populate options for each filter
        endYears.forEach(function(year) {
            endYearFilter.append('<option value="' + year + '">' + year + '</option>');
        });
        topics.forEach(function(topic) {
            topicFilter.append('<option value="' + topic + '">' + topic + '</option>');
        });
        sectors.forEach(function(sector) {
            sectorFilter.append('<option value="' + sector + '">' + sector + '</option>');
        });
        regions.forEach(function(region) {
            regionFilter.append('<option value="' + region + '">' + region + '</option>');
        });
    }

    // Helper function to get unique values of a field from fetched data
    function getUniqueFieldValues(field, data) {
        var uniqueValues = [];
        data.forEach(function(item) {
            if (uniqueValues.indexOf(item[field]) === -1) {
                uniqueValues.push(item[field]);
            }
        });
        return uniqueValues;
    }

    // Function to render all charts based on fetched data
    function renderCharts(data) {
        renderIntensityChart(data);
        renderYearlyTrendsChart(data);
        renderCountryIntensityMap(data);
    }

    // Function to render Intensity Distribution (Bar Chart)
    function renderIntensityChart(data) {
        var countries = getUniqueFieldValues('country', data);
        var intensityValues = countries.map(function(country) {
            var totalIntensity = data
                .filter(function(item) {
                    return item.country === country;
                })
                .reduce(function(acc, curr) {
                    return acc + curr.intensity;
                }, 0);

            return {
                x: [country],
                y: [totalIntensity],
                type: 'bar',
                name: country
            };
        });

        var layout = {
            title: 'Total Intensity by Country',
            xaxis: {
                title: 'Country'
            },
            yaxis: {
                title: 'Total Intensity'
            }
        };

        Plotly.newPlot('intensity-chart', intensityValues, layout);
    }

    // Function to render Yearly Trends (Line Chart)
    function renderYearlyTrendsChart(data) {
        var years = getUniqueFieldValues('year', data);
        var intensityTrends = years.map(function(year) {
            var yearData = data.filter(function(item) {
                return item.year === year;
            });
            var totalIntensity = yearData.reduce(function(acc, curr) {
                return acc + curr.intensity;
            }, 0);

            return {
                x: [year],
                y: [totalIntensity],
                mode: 'lines+markers',
                name: year
            };
        });

        var layout = {
            title: 'Total Intensity by Year',
            xaxis: {
                title: 'Year'
            },
            yaxis: {
                title: 'Total Intensity'
            }
        };

        Plotly.newPlot('yearly-trends-chart', intensityTrends, layout);
    }

    // Function to render Country Intensity Map (Bar Chart)
    function renderCountryIntensityMap(data) {
        var countries = getUniqueFieldValues('country', data);
        var countryIntensities = countries.map(function(country) {
            var intensity = data.find(function(item) {
                return item.country === country;
            }).intensity;

            return {
                x: [country],
                y: [intensity],
                type: 'bar',
                name: country
            };
        });

        var layout = {
            title: 'Intensity by Country',
            xaxis: {
                title: 'Country'
            },
            yaxis: {
                title: 'Intensity'
            }
        };

        Plotly.newPlot('country-intensity-chart', countryIntensities, layout);
    }

    // Event listener for filter changes
    $('#endYearFilter, #topicFilter, #sectorFilter, #regionFilter').change(function() {
        var filters = {
            end_year: $('#endYearFilter').val(),
            topic: $('#topicFilter').val(),
            sector: $('#sectorFilter').val(),
            region: $('#regionFilter').val()
        };
        fetchFilteredInsights(filters);
    });
});
