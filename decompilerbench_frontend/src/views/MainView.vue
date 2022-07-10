<template>
  <v-container
    cols="12"
    class="fill-height pb-4"
    >
    
    <v-row no-gutters class="fill-height fill-width">

      <v-col
        cols="12"
        sm="4"
        md="4"
        lg="4"
        class="pa-2 fill-width"
      >

        <v-btn
          ref="btnPredict"
          color="primary"
          class="mb-4"
          :loading="isBtnCompileLoading"
          @click="btnCompileClick"
        >
          Compile
        </v-btn>

        <v-combobox
          clearable
          outlined
          v-model="selected_sample"
          :items="samples"
        ></v-combobox>
        <v-textarea
          outlined
          name="input-7-4"
          label="Исходный код на Си"
          :value="c_code"
          class="fill-height"
          
          auto-grow
          rows="14"
        ></v-textarea>

        <!-- <audio-player
          url="https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_5MG.mp3"
          playerid="audio-player"
        > </audio-player> -->



      </v-col>

      <v-col
        cols="12"
        sm="4"
        md="4"
        lg="4"
        class="pa-2"
      >
        <v-btn
          ref="btnPredict"
          class="mb-4"
          color="primary"
          :loading="isBtnPredictLoading"
          @click="btnPredictClick"
          :disabled="!isCompiled"
        >
          Decompile
        </v-btn>
        
        <v-textarea
          outlined
          label="Скомпилированный код на Asm"
          v-model="asm_code"
          readonly
          class="fill-height"
          auto-grow
          rows="18"
        ></v-textarea>
        

      </v-col>
      <v-col
        cols="12"
        sm="4"
        md="4"
        lg="4"
        class="pa-2"
        fill-height
      >
        <v-textarea
          outlined
          label="Декомпилированный код на Asm"
          class="fill-height"
          :value="disasm_code"
          readonly
          auto-grow
          rows="20"
        ></v-textarea>
      </v-col>
    </v-row>

    <v-snackbar
      v-model="showmessage"
      timeout="2000"
      color="red accent-2"
    >
      {{ messagetext }}

      <template v-slot:action="{ attrs }">
        <v-btn
          color="white"
          text
          v-bind="attrs"
          @click="showmessage = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>

// import { throws } from 'assert';
import axios from 'axios'

export default {
  name: 'MainView',
  components: {

  },
  data () {
    console.log("data: this.$route.params = ", this.$route.params.sndfiles);
    return {
      // soundFiles :[
      //   {name:"orig_sound1.wav", url:"/orig_sound.wav"},
      //   {name:"orig_sound2.wav", url:"/orig_sound2.wav"},
      //   {name:"orig_sound3.wav", url:"/orig_sound3.wav"},
      //   {name:"orig_sound4.wav", url:"/orig_sound4.wav"},
      //   {name:"orig_sound5.wav", url:"/orig_sound5.wav"}
      // ],
      c_code : "#include <iostream.h>",
      asm_code : "",
      disasm_code : "",
      selectedfile : 0,
      recognizedtext : null,
      completed : 50,
      method : 0,
      isBtnPredictLoading : false,
      isBtnCompileLoading : false,
      selected_sample : "",
      samples : ["example1.c", "example2.c", "example3.c"],
      isCompiled : false,
      uploadLoading : true,
      showmessage : false,
      messagetext : "",
      soundfileurl : null,

      soundfiles_table :{
        "original":[
          {name:"orig_sound1.wav", url:"/orig_sound1.wav"},
          {name:"orig_sound2.wav", url:"/orig_sound2.wav"},
          {name:"orig_sound3.wav", url:"/orig_sound3.wav"},
          {name:"orig_sound4.wav", url:"/orig_sound4.wav"},
          {name:"orig_sound5.wav", url:"/orig_sound5.wav"}
        ],
        "adversarial":[
          {name:"adv_sound1.wav", url:"/adv_sound1.wav"},
          {name:"adv_sound2.wav", url:"/adv_sound2.wav"},
          {name:"adv_sound3.wav", url:"/adv_sound3.wav"},
          {name:"adv_sound4.wav", url:"/adv_sound4.wav"},
          {name:"adv_sound5.wav", url:"/adv_sound5.wav"}
        ],
      },

      // soundfiles : (typeof(this.$router.params)==='undefined' || this.$router.params === null)
      //   ? "original"
      soundfiles  : this.$route.params.sndfiles,
    }
  },
  methods: {
    soundFileSelected(p_url){
      this.soundfileurl = p_url;
    },

    btnCompileClick(){
      this.isBtnCompileLoading = true;
      axios.post("/compile", {params:{
        c_code : this.c_code,
      }})
      .then(response => {
        if(response.data.status == "ok"){
          //
          this.isCompiled = true;
          this.asm_code = response.data.asm_code;
        }
        else{
          //
        }
        console.log("response = ", response)
        this.isBtnCompileLoading = false;
      })
      .catch(error => {
        console.log("error=",error);
        this.messagetext = error;
        this.showmessage = true;
        this.isBtnCompileLoading = false;
      })
      .finally(() => {
        console.log("finally");
        this.isBtnCompileLoading = false;
      });
    },

    btnPredictClick(){
      this.isBtnPredictLoading = true;
      axios.post("/decompile", {params:{
        asm_code : this.asm_code,
      }})
      .then(response => {
        if(response.data.status === "ok"){
          this.disasm_code = response.data.disasm_code;
        }
        else{
          //
        }
        console.log("response = ", response)
        this.isBtnPredictLoading = false;
      })
      .catch(error => {
        console.log("error=",error);
        this.messagetext = error;
        this.showmessage = true;
        this.isBtnPredictLoading = false;
      })
      .finally(() => {
        console.log("finally");
        this.isBtnPredictLoading = false;
      });
    },

  },
  // watch : {
  //   'this.$router.params': function (params){
  //     console.log("watch, this.$router.params.sndfiles= ", this.$router.params.sndfiles);
  //     this.$forceUpdate();
  //   }
  // },
  // mounted(){
  //   console.log("mounted, this.$router.params= ", this.$router.params);
  // }
}
</script>
