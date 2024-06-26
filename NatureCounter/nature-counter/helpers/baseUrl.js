import { Platform } from "react-native";

const baseUrl = Platform.OS === 'android'
? 'http://192.168.0.15:80/'
: 'http://127.0.0.1:8000/';

export default baseUrl;