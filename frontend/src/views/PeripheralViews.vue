<template>
  <div>
    <div class="container">
      <div class="nametag">
        <p>주변기기</p>
        <img :src="peripheralIcon" alt="" />
      </div>
      <div class="menu-groups">
        <v-btn-toggle v-model="toggle" class="btns">
          <v-btn
            v-for="item in buttonItems"
            :key="item.value"
            :value="item.value"
            :class="{
              'active-button': toggle === item.value,
              'inactive-button': toggle !== item.value,
            }"
            @click="setToggle(item.value)"
          >
            {{ item.label }}
          </v-btn>
        </v-btn-toggle>
        <div class="searchbar">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="검색"
            id="searchbar-inner"
            @keyup.enter="goSearch"
            class="searchbar-inner"
          />
          <img
            :src="searchIcon"
            alt="돋보기"
            @click="goSearch"
            class="searchmark"
          />
        </div>
      </div>
    </div>
    <KeyboardComponentVue v-if="toggle === 'keyboard'" />
    <MouseComponentVue v-if="toggle === 'mouse'" />
    <MonitorComponentVue v-if="toggle === 'monitor'" />
    <PrinterComponentVue v-if="toggle === 'printer'" />
    <EtcComponentVue v-if="toggle === 'etc'" />
    <footer>
      <div class="footer-back"></div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { peripheralIcon } from "@/assets/Icon";
import { searchIcon } from "@/assets/Icon";
import KeyboardComponentVue from "../components/PeripheralViewComponents/KeyboardComponent.vue";
import MouseComponentVue from "../components/PeripheralViewComponents/MouseComponent.vue";
import MonitorComponentVue from "../components/PeripheralViewComponents/MonitorComponent.vue";
import PrinterComponentVue from "../components/PeripheralViewComponents/PrinterComponent.vue";
import EtcComponentVue from "../components/PeripheralViewComponents/EtcComponent.vue";

const toggle = ref("keyboard");

const setToggle = (value) => {
  toggle.value = value;
  console.log(toggle);
};

const buttonItems = [
  { label: "키보드", value: "keyboard" },
  { label: "마우스", value: "mouse" },
  { label: "모니터", value: "monitor" },
  { label: "프린터 / 복합기", value: "printer" },
  { label: "기타", value: "etc" },
];

const searchQuery = ref("");

const goSearch = () => {
  // 검색을 수행하는 로직을 여기에 추가
  console.log("검색어:", searchQuery.value);

  // 검색 후 입력 내용 초기화
  searchQuery.value = "";
};
</script>

<style scoped>
.container {
  margin-top: 5%;
  margin-left: 5%;
  margin-right: 5%;
  display: flex;
  position: relative;
}

.nametag {
  width: 150px;
  height: 150px;
  flex-shrink: 0;
  border-radius: 10px;
  background: var(--Color, #fff);
  box-shadow: 0px 0px 1px 1px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.nametag p {
  color: #000;
  font-family: Inter;
  font-size: 20px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  margin-top: 21px;
}

.nametag img {
  width: 61px;
  height: 58px;
  margin-top: 18px;
}

.menu-groups {
  display: flex;
  flex-direction: column;
  width: 100%;
  justify-content: space-between;
  margin-left: 5%;
}

.btns {
  display: flex;
  justify-content: space-evenly;
}

.active-button {
  font-size: 14px;
  font-style: normal;
  font-weight: 700;
  color: #fff;
  background: #d9d9d9;
  border-radius: 30px !important;
  height: 50px;
  width: 18%;
  background-color: #4599fc; /* 활성화된 버튼의 색상 설정 */
}

.inactive-button {
  font-size: 14px;
  font-style: normal;
  font-weight: 700;
  color: #fff;
  background: #d9d9d9;
  border-radius: 30px !important;
  height: 50px;
  width: 18%;
}

.searchbar {
  margin: auto;
  margin-top: 0px;
  margin-bottom: 0px;
  width: 50%;
  position: relative;
  display: inline-block;
}

.searchbar-inner {
  box-shadow: 2px 2px 5px 2px #c9c9c9;
  height: 2.5rem;
  width: 100%;
  border: 1px;
  border-radius: 20px;
  padding: 0px 20px;
  padding-right: 40px; /* 이미지를 우측에 표시하기 위한 오른쪽 패딩 추가 */
}

.searchmark {
  position: absolute;
  height: 2rem;
  width: 2rem;
  cursor: pointer;
  position: absolute;
  top: 50%;
  right: 8px; /* 이미지를 우측으로 이동 */
  transform: translateY(-50%);
  width: 2.5rem; /* 이미지의 크기 조정 (원하는 크기로 설정) */
  height: 2.5rem;
  cursor: pointer; /* 마우스 커서 모양을 포인터로 변경하여 클릭 가능한 것처럼 보이게 함 */
}

.footer-back {
  margin-top: 50px;
  background-color: #000;
  height: 300px;
}
</style>
