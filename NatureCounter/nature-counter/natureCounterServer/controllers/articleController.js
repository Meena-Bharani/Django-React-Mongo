// const mongoose = require('mongoose');
//const createError = require('http-errors');
// const Articles = require('../models/articleSchema');

import createError from 'http-errors';

const [Articles,setArticles] = useState([])
useEffect(()=> {
    fetch(`${baseUrl}article`, {
        method: "GET"
    })
    .then(resp => resp.json())
    .then(data => {
      setArticles(data)
    })
    .catch(error => Alert.alert("error"+error))
  },[])

export async function getAllArticles(req, res, next) {
    try {
        const article = await Articles.find(req.query);
        res.json(article);
    } catch (err) {
        console.log(err.message);
        next(err);
    }
}
export async function postArticles(req, res, next) {
    try {
        const newArticle = new Articles(req.body);
        const savedArticle = await newArticle.save();
        res.json(savedArticle);
    } catch (err) {
        console.log(err.message);
        next(err);
    }
}
export async function deleteAllArticles(req, res, next) {
    try {
        const delArticle = await Articles.deleteMany({});
        res.json(delArticle);
    } catch (err) {
        console.log(err.message);
        next(err);
    }
}
export async function getArticleById(req, res, next) {
    const id = req.params.articleId;
    try {
        const article = await Articles.findById(id);
        if (!article) {
            throw createError(404, 'Article does not exits');
        } else {
            res.json(article);
        }
    } catch (err) {
        console.log(err.message);
        next(err);
    }
}
export async function updateArticleById(req, res, next) {
    const id = req.params.articleId;
    try {
        const article = await Articles.findByIdAndUpdate(id, {
            $set: req.body
        }, { new: true });
        if (!article) {
            throw createError(404, 'Article does not exits');
        } else {
            res.json(article);
        }
    } catch (err) {
        console.log(err.message);
        next(err);
    }
}
export async function deleteArticleById(req, res, next) {
    const id = req.params.articleId;
    try {
        const article = await Articles.findByIdAndRemove(id);
        res.json();
    } catch (err) {
        console.log(err.message);
        next(err);
    }
}