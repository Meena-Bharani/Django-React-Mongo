import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Alert, FlatList, StyleSheet, Text, View, Colors } from 'react-native';
import { useState, useEffect } from 'react';
import baseUrl from './helpers/baseUrl';

export default function App() {
  const [articles,setArticles] = useState([])

  useEffect(()=> {
    fetch(`${baseUrl}article`, {
    //fetch('http://192.168.0.15:80/article', {
    //fetch('http://172.20.20.20:80/article', {
        method: "GET"
    })
    .then(resp => resp.json())
    .then(data => {
      console.log(data)
      setArticles(data)
    })
    .catch(error => Alert.alert("error"+error))
  },[])

  const renderArticleData = (item) => {
    return (
      <View style={styles.container}>
        <Text style={styles.textStyle}>{item.title}</Text>
      </View>
    )
  }

  return (
    /*
    <View style={styles.mainCardView}>
          <View style={{flexDirection: 'row', alignItems: 'center'}}>
            <View style={styles.subCardView}></View>
            <View style={{marginLeft: 12}}></View>
            </View>
    </View>
    */
    <View style={styles.container}>
      <FlatList style={styles.textStyle}
        data ={articles}
        renderItem = {({item}) => {
          return renderArticleData(item)
        }}
        keyExtractor = {item =>`${item.id}`} //covert id to string ``
      />

      <Text>Nature Counter App!</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  textStyle:{
    fontSize:25,
    color:'black',
  },
  maincontainer: {
    height: 90,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'white',
    borderRadius: 15,
    shadowColor: 'black',
    shadowOffset: {width: 0, height: 0},
    shadowOpacity: 1,
    shadowRadius: 8,
    elevation: 8,
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingLeft: 16,
    paddingRight: 14,
    marginTop: 6,
    marginBottom: 6,
    marginLeft: 16,
    marginRight: 16,
  },
  subCardView: {
    height: 50,
    width: 50,
    borderRadius: 25,
    backgroundColor: 'gray',
    borderColor: '#eeeeee',
    borderWidth: 1,
    borderStyle: 'solid',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
