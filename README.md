# Hafezah-Task

## APIs
* URL: `http://ec2-3-83-160-100.compute-1.amazonaws.com`

### Register Owner
* Path: `/owner/register`
* Method: POST
* Body:
```
{
  "email": "test@test.com",
  "username": "tester",
  "password": "tester"
}
```
* Response:
```
{
  "token": "Bearer ..."
}
```

### Auth Owner
* Path: `/owner/auth`
* Method: POST
* Body: 
```
{
  "username": "tester",
  "password": "tester"
}
```
* Response:
```
{
  "token": "Bearer ..."
}
```

### Create Restaurant
* Path: `/restaurants`
* Method: POST
* Headers:
```
{
  "Authorization": "Bearer ..."
}
```
* Body:
```
{
  "name": "test",
  "longitude": 3.000156,
  "latitude": 4.00025,
  "phoneNumber": "015066"
}
```
* Response:
```
{
  "id": 1,
  "name": "agian2"
  "latitude": 4.001,
  "longitude": 3.5005,
  "phoneNumber": "1326"
}
```

### Edit Restaurant
* Path: `/restaurants`
* Method: PATCH
* Headers:
```
{
  "Authorization": "Bearer ..."
}
```
* Body:
```
{
  "name": "test",
  "longitude": 3.000156,
  "latitude": 4.00025,
  "phoneNumber": "015066"
}
```
* Response:
```
{
  "id": 1,
  "name": "agian2"
  "latitude": 4.001,
  "longitude": 3.5005,
  "phoneNumber": "1326"
  "logo": "http://hafezah-task.s3.amazonaws.com/logo.jpg"
}
```

### Upload Restaurant Logo
* Path: `/restaurants/logo/Upload`
* Method: POST
* Headers:
```
{
  "Authorization": "Bearer ..."
}
```
* Body: image file
* Response:
```
{
  "url": "http://hafezah-task.s3.amazonaws.com/logo.jpg"
}
```
### Nearby Restaurants
* Path: `/restaurants/nearby`
* Method: GET
* Query: `?long=3.5&lat=4`
* Response:
```
[
  {
    "id": 1,
    "name": "agian2"
    "latitude": 4.001,
    "longitude": 3.5005,
    "phoneNumber": "1326"
    "logo": "http://hafezah-task.s3.amazonaws.com/logo.jpg"
  },
  {
    "id": 2,
    "name": "agian2"
    "latitude": 4.001,
    "longitude": 3.5005,
    "phoneNumber": "1326"
    "logo": "http://hafezah-task.s3.amazonaws.com/logo.jpg"
  }
]
```

### Direction to Restaurant
* Path `/restaurants/direction`
* Method: GET
* Query: `?from_long=3.5&from_lat=4&to_long=3.5001&to_lat=4.001`
* Response: map.html
