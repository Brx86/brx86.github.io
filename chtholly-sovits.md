# Sovits 4.0 珂朵莉模型使用方法 

## 配置 Sovits

```bash
git clone https://github.com/svc-develop-team/so-vits-svc sovits-4.0
cd sovits-4.0
mkdir chtholly
conda create -n sovits python=3.8.16 -y
conda activate sovits
conda install Flask Flask_Cors gradio numpy pyworld tqdm onnx librosa pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia -c conda-forge
pip install PyAudio SoundFile scikit-maad praat-parselmouth onnxsim onnxoptimizer fairseq==0.12.2
```

## 下载 hubert 模型

contentvec ：[checkpoint_best_legacy_500.pt](https://ibm.box.com/s/z1wgl1stco8ffooyatzdwsqn2psd9lrr) 放在 `hubert`​ ​目录下

## 下载珂朵莉模型

地址：[https://drive.google.com/drive/folders/1YzC6XAtXiTsAIzrzrQGhybBFZnGwhf7j](https://drive.google.com/drive/folders/1YzC6XAtXiTsAIzrzrQGhybBFZnGwhf7j)

将其中的 `config.json`​ `G_10400.pth`​ `kmeans_10000.pt`​ 放在 `chtholly`​ 目录下（也可以放在别的地方，自己记住就行）

## 开始推理

在 `raw`​ 目录下放入将要转换的音频文件（如 `和服鲁道夫象征.wav`​ ）

执行：

```bash
python inference_main.py -a -m chtholly/G_10400.pth -c chtholly/config.json -s Chtholly-vol -cm chtholly/kmeans_10000.pt -cr 0.2 -n 和服鲁道夫象征.wav 
```

等待完成，就可以在 `results`​ 目录下找到转换完成的文件了

关于各参数的含义：[Readme.md](https://github.com/innnky/so-vits-svc/tree/4.0#%E6%8E%A8%E7%90%86)

> 必填项部分
>
> * -m, --model_path：模型路径。
> * -c, --config_path：配置文件路径。
> * -n, --clean_names：wav 文件名列表，放在 raw 文件夹下。
> * -t, --trans：音高调整，支持正负（半音）。
> * -s, --spk_list：合成目标说话人名称。
>
> 可选项部分：见下一节
>
> * -a, --auto_predict_f0：语音转换自动预测音高，转换歌声时不要打开这个会严重跑调。
> * -cm, --cluster_model_path：聚类模型路径，如果没有训练聚类则随便填。
> * -cr, --cluster_infer_ratio：聚类方案占比，范围 0-1，若没有训练聚类模型则填 0 即可。
