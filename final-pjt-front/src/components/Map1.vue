<template>
  <div class="map_box">
    <div class="map_b">
    <div id="map" style="width:700px;height:500px;"></div>
    <div class="search_bank">
      <div class="title">🏦 집 주변 은행 찾기</div>
      <hr>
      <div class="desc"></div>
      <input type="text" v-model="addr" placeholder="서울특별시 강남구" class="addr input-group flex-nowrap form-control">
      <select class="form-select" id="bank" v-model="bank">
      <option value="">-- 은행 선택 --</option>
      <option value="국민은행">국민은행</option>
        <option value="광주은행">광주은행</option>
        <option value="경남은행">경남은행</option>
        <option value="농협은행주식회사">농협은행주식회사</option>
        <option value="대구은행">대구은행</option>
        <option value="부산은행">부산은행</option>
        <option value="수협은행">수협은행</option>
        <option value="신한은행">신한은행</option>
        <option value="우리은행">우리은행</option>
        <option value="전북은행">전북은행</option>
        <option value="주식회사 케이뱅크">주식회사 케이뱅크</option>
        <option value="주식회사카카오뱅크">주식회사카카오뱅크</option>
        <option value="중소기업은행">중소기업은행</option>
        <option value="제주은행">제주은행</option>
        <option value="토스뱅크 주식회사">토스뱅크 주식회사</option>
        <option value="하나은행">하나은행</option>
        <option value="한국산업은행">한국산업은행</option>
        <option value="한국스탠다드차타드은행">한국스탠다드차타드은행</option>
    </select>
    <button @click = "initMap" class="btn btn-primary search_btn">검색</button>
    </div>
  </div>
  </div>
</template>


<script setup>
import { onMounted } from 'vue';

let map = null;
let addr = '';
let bank = '';
let lat = 37.5008104
let lon = 127.0376574

const initMap = function () {
  let myCenter = new kakao.maps.LatLng(lat, lon);

  if (!(addr==='') && !(bank==='')) { 
    const geocoder = new kakao.maps.services.Geocoder();

    geocoder.addressSearch(`${addr}`, function(result, status) {
    
     if (status === kakao.maps.services.Status.OK) {
        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
        map.setCenter(coords);
    } 
    })
    
    var ps = new kakao.maps.services.Places(); 
    ps.keywordSearch(`${addr + bank}`, placesSearchCB); 
    
    function placesSearchCB (data, status, pagination) {
        if (status === kakao.maps.services.Status.OK) {
    
            var bounds = new kakao.maps.LatLngBounds();
    
            for (var i=0; i<data.length; i++) {
                displayMarker(data[i]);    
                bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
            }
        }
    }
    
    var infowindow = new kakao.maps.InfoWindow({zIndex:1});
    function displayMarker(place) {
        
        var marker = new kakao.maps.Marker({
            map: map,
            position: new kakao.maps.LatLng(place.y, place.x) 
        });

        marker.setMap(map)
        
        kakao.maps.event.addListener(marker, 'click', function() {
            infowindow.setContent(
              '<div style="padding:5px;font-size:12px;">'
                + place.place_name + '<br>' + place.road_address_name + '</div>'
            );
            infowindow.open(map, marker);
        });
    }
    
  } else if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((position) => {
      lat = position.coords.latitude;
      lon = position.coords.longitude;
      myCenter = new kakao.maps.LatLng(lat, lon);
      new kakao.maps.Marker({
        map,
        position: myCenter,
      });
      map.setCenter(myCenter);
    });
  }

  const container = document.getElementById("map");
  const options = {
    center: myCenter,
    level: 6,
  };
  map = new kakao.maps.Map(container, options);

  const zoomControl = new kakao.maps.ZoomControl();
  map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
};

onMounted(() => {
  if (window.kakao && window.kakao.maps) {
    initMap();
  } else {
    const script = document.createElement('script');
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${
      import.meta.env.VITE_MAP_API_KEY
    }&libraries=services`;
    script.addEventListener('load', () => {
      kakao.maps.load(initMap);
    });
    document.head.appendChild(script);
  }
});
</script>


<style scoped>
.map_box {
  margin-top: 30px;
  display: flex;
  justify-content: center;
}
.map_b {
  width: 1200px;
  display: flex;
}
.title {
  font-weight: bold;
  font-size: 25px;
}
.desc {
  margin-bottom: 10px;
  font-size: 15px;
}
.addr {
  margin: 10px 0px;
  padding: 10px;
}

.search_bank {
  width: 400px;
  display: flex;
  flex-direction: column;
  margin: 0 30px;
  background-color: #f7f7f7;
  border-radius: 10px;
  padding: 20px;
}

#bank {
  margin: 10px 0;
  padding: 10px;
}

.search_btn {
  margin-top: 20px;
  padding: 10px;
}
</style>