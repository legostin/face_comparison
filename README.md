# Face comparison micro-service

## Installation

#### Using Docker
    $ git clone https://github.com/legostin/face_comparison.git
    $ docker build ./ -t facerec
    $ docker run -d -p 6000:6000 --name facerecognition -it facerec 

Теперь приложение для распознования лиц доступно на локальном 6000 порту и в настройках нджинкс его можно повесить на поддомен или отдельный роут

#### Clone

    $ git clone https://github.com/legostin/face_comparison.git
    
#### Install dependencies

    $ pip3 install -r requirements.txt
    
#### Set up models

To use default models:
1. Install dlib (requires cmake): `$ pip install dlib`
2. Fetch model pre-trained files: `$ fetch_models`

To use custom models, configure `.env`.
        
    
#### Development server

    flask run

#### Deployment

To _deploy_ see flask [deployment options](https://flask.palletsprojects.com/en/1.1.x/deploying/)  


##
 **Sample Call:**
  ```
    curl -X POST [host:port]/api/compare_faces \
        -F source=@face_image1.jpg \
        -F target=@face_image2.jpg
  ```