// API endpoint and task ID
// const apiUrl = 'https://graph.microsoft.com/v1.0/me/todo/lists/AQMkADAwATM3ZmYAZS0wZmQ2LTA0MGQtMDACLTAwCgAuAAADsbzhU0ri70i_oUw8Yy_bAwEA6ivYBau8iU_kPd0Y4LosnQAFQ4C96gAAAA==/tasks/<AQMkADAwATM3ZmYAZS0wZmQ2LTA0MGQtMDACLTAwCgBGAAADsbzhU0ri70i_oUw8Yy_bAwcA6ivYBau8iU_kPd0Y4LosnQAFQ4C96gAAAOor2AWrvIlPpD3dGOC6LJ0ABUOA2VEAAAA=';
// const accessToken = 'EwBwA8l6BAAUAOyDv0l6PcCVu89kmzvqZmkWABkAAZiKHORrQf6BhiG3P8vhYz3yLBf6Vi+iGR7qdzNGcQqnEPhjtFa+wbXRSwavbHpEe0oa0yEDCSG4wlGHeR6KglAaoMVsnphEZCwLhU16Rz27sipjfoD+z0TGqqrQhUwLIq4u02ByMHa25OPcEB5Wo/4SKA3+7cKN3qG7AMstz3ZT69nnOEd3Ko8hVFXmKDrQ9pjtE0C9u6hSr4vy4eZuNefg03aDVtg+SjXDFEctJEL4Mq5H5U3yNG0h9eT/KbcFzKDNH8+4q83jadkYfkHySLQ7v23TzTzcB57Uarpu3nEjwe2bP0YDqE829OEyoj76XkR5iNlnxXFyQftR8TNz0McDZgAACFv7XQ5rEyIPQAKfC4y0SNI2Tdv05ESmVbXoILsWHrlX1P9YYqwe6+s48gK+Rc5FH3uTFcy/kfhuBx62DiU2xb5xe9e+ALmiTual0GaaQZsOI2pVcslBG6h91C/Dg+nccQNVHptB2O1IVFPoUih2npUcMr8H9HiDTlBWYLVlldLv9KkOwl33L0QarMnoCNWjc2yqHF9DmTspoyjhIuD8jYovNzY2RKX44eFj3ybk3aWJiGOIAt2SnjbwOw3Sk05NQPMFSYkj40u8auxxBbGv7YXc6fR18E5Gac6XUIuXU5EmsXzhm9iLZA5gVPYm5psOBJCP8WlpuoWiZbg81r/+wT/7y4KeEzZmilAMhkmYE5gbleC0kXUUpT1J8wXcW1oECFZ6qPnXcuMD5Gev2fjwixdTtXB/4FVK0NS6DL4E3gcksTtIuHkGqQeptHAd6DuNcXBbN2I7GmoR/PX4GyjkCcJ5VrPV8yoowqvhbxKeuVISIgc/cKnOqZEo0IhYBxYUE/Vde7T1pkFY87nKAlexJFUpGlqO7CE/Gfl2G2sb94ELgXs0Xf+FHoH0fWIA0mLgMrPrFPf7/J6jefFaxw+QQBHS/8K8JMt9P7nYhLn+aDMM+R5HIjURXIygXoodqqatAlaDTA0t/lUcuiZfd02wivNpESDerXpKKqav5obsYTYaW3VIPoDt4uspBy50OAvSWYJQ6yewDqVbKWxs15uhxsS0MwczLhFzJlZB76yyJdRPhrJhX0kvRI834jGc8XlPUUZmWpeyTsS18qGIAg==';

// // Fetch task details
// fetch(apiUrl, {
//     headers: {
//         'Authorization': `Bearer ${accessToken}`
//     }
// })
// .then(response => response.json())
// .then(task => {
//     // Display task details
//     const taskDetailsDiv = document.getElementById('taskDetails');
//     taskDetailsDiv.innerHTML = `
//         <h2>${task.title}</h2>
//         <p>Status: ${task.status}</p>
//         <p>Completed Date: ${task.completedDateTime.dateTime}</p>
//     `;
// })
// .catch(error => {
//     console.error('Error fetching task details:', error);
// });


const accessToken = 'EwBwA8l6BAAUAOyDv0l6PcCVu89kmzvqZmkWABkAAZiKHORrQf6BhiG3P8vhYz3yLBf6Vi+iGR7qdzNGcQqnEPhjtFa+wbXRSwavbHpEe0oa0yEDCSG4wlGHeR6KglAaoMVsnphEZCwLhU16Rz27sipjfoD+z0TGqqrQhUwLIq4u02ByMHa25OPcEB5Wo/4SKA3+7cKN3qG7AMstz3ZT69nnOEd3Ko8hVFXmKDrQ9pjtE0C9u6hSr4vy4eZuNefg03aDVtg+SjXDFEctJEL4Mq5H5U3yNG0h9eT/KbcFzKDNH8+4q83jadkYfkHySLQ7v23TzTzcB57Uarpu3nEjwe2bP0YDqE829OEyoj76XkR5iNlnxXFyQftR8TNz0McDZgAACFv7XQ5rEyIPQAKfC4y0SNI2Tdv05ESmVbXoILsWHrlX1P9YYqwe6+s48gK+Rc5FH3uTFcy/kfhuBx62DiU2xb5xe9e+ALmiTual0GaaQZsOI2pVcslBG6h91C/Dg+nccQNVHptB2O1IVFPoUih2npUcMr8H9HiDTlBWYLVlldLv9KkOwl33L0QarMnoCNWjc2yqHF9DmTspoyjhIuD8jYovNzY2RKX44eFj3ybk3aWJiGOIAt2SnjbwOw3Sk05NQPMFSYkj40u8auxxBbGv7YXc6fR18E5Gac6XUIuXU5EmsXzhm9iLZA5gVPYm5psOBJCP8WlpuoWiZbg81r/+wT/7y4KeEzZmilAMhkmYE5gbleC0kXUUpT1J8wXcW1oECFZ6qPnXcuMD5Gev2fjwixdTtXB/4FVK0NS6DL4E3gcksTtIuHkGqQeptHAd6DuNcXBbN2I7GmoR/PX4GyjkCcJ5VrPV8yoowqvhbxKeuVISIgc/cKnOqZEo0IhYBxYUE/Vde7T1pkFY87nKAlexJFUpGlqO7CE/Gfl2G2sb94ELgXs0Xf+FHoH0fWIA0mLgMrPrFPf7/J6jefFaxw+QQBHS/8K8JMt9P7nYhLn+aDMM+R5HIjURXIygXoodqqatAlaDTA0t/lUcuiZfd02wivNpESDerXpKKqav5obsYTYaW3VIPoDt4uspBy50OAvSWYJQ6yewDqVbKWxs15uhxsS0MwczLhFzJlZB76yyJdRPhrJhX0kvRI834jGc8XlPUUZmWpeyTsS18qGIAg==';
const apiUrl = 'https://graph.microsoft.com/v1.0/me/todo/lists/AQMkADAwATM3ZmYAZS0wZmQ2LTA0MGQtMDACLTAwCgAuAAADsbzhU0ri70i_oUw8Yy_bAwEA6ivYBau8iU_kPd0Y4LosnQAFQ4C96gAAAA==/tasks/<AQMkADAwATM3ZmYAZS0wZmQ2LTA0MGQtMDACLTAwCgBGAAADsbzhU0ri70i_oUw8Yy_bAwcA6ivYBau8iU_kPd0Y4LosnQAFQ4C96gAAAOor2AWrvIlPpD3dGOC6LJ0ABUOA2VEAAAA=';

fetch(apiUrl, {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${accessToken}`
    }
})
Application (client) ID
ad57a6c5-ec89-407b-aa46-462755df5cd1
Object ID
9cf33fc0-85e3-417d-b1c3-00ad63822552
Directory (tenant) ID
a6ba99e9-fe46-43b3-9608-63c4215ceb52

value
x3B8Q~Y32XaC4OrwNTBj9oMphNI6ObH.ZMV08b44

secret_id
b699016a-c672-415f-96f4-c31916c8f0b6
.then(response => response.json())
.then(taskData => {
    // Handle the task data here
    console.log(taskData);
})
.catch(error => {
    console.error('Error fetching task data:', error);
});

https://login.microsoftonline.com/a6ba99e9-fe46-43b3-9608-63c4215ceb52/adminconsent?client_id=ad57a6c5-ec89-407b-aa46-462755df5cd1&redirect_id=https%3A%2F%2Flocalhost%2Fmyapp%2Fpermissions&state=12345