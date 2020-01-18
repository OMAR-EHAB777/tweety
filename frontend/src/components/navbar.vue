<template>
   <nav class="navbar navbar-expand-md navbar-dark fixed-top" id="banner">

  <!-- Brand -->
       <div class="container">
              <a><router-link
                    :to="{ name: 'home' }"
                    class="navbar-brand"
                    >Tweety
                  </router-link></a>

  <!-- Toggler/collapsibe Button -->
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>

  <!-- Navbar links -->
          <div class="collapse navbar-collapse" id="collapsibleNavbar">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item">
                 <router-link
              :to="{ name: 'home' }"

              >Home<i class="fa fa-home"> </i>
            </router-link>
              </li>
              <li class="nav-item">
               <router-link
              :to="{ name: 'about' }"

              >Explore<i class="fas fa-hashtag"></i>
            </router-link>
              </li>
              <li class="nav-item">
                <router-link
              :to="{ name: 'example' }"

                >Notification<i class="fa fa-globe"></i>
            </router-link>
              </li>
              <li class="nav-item">
                <router-link
              :to="{ name: 'tweety-editor' }"

                >tweety<i class="fas fa-envelope"></i>
            </router-link>
              </li>
               <!-- Dropdown -->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
                account
              </a>
              <div class="dropdown-menu">
                <a class="dropdown-item" href="#">profile</a>
                <a class="dropdown-item" href="#">bookmarks</a>
                <a class="dropdown-item" href="#">settings</a>
              </div>
            </li>
            </ul>
          </div>
</div>
</nav>

</template>
<script>
    export default{
        name : "NavbarComponent"
    }
</script>
<style>
.navbar-brand  span{
	color: #17adf6;
	font-size:25px;font-weight:700;letter-spacing:0.1em;
    font-family: 'Kaushan Script','Helvetica Neue',Helvetica,Arial,cursive;
}
.navbar-brand {
	color: #3eb1ff;
	font-size:25px;
    font-family: 'Kaushan Script','Helvetica Neue',Helvetica,Arial,cursive;
	font-weight:700;
	letter-spacing:0.1em;
}

.navbar-nav .nav-item .nav-link{
	padding: 1.1em 1em!important;
	font-size: 120%;
    font-weight: 500;
    letter-spacing: 1px;
    color: #fff;
   font-family: 'Gothic A1', sans-serif;
}
.navbar-nav .nav-item .nav-link:hover{color:#fed136;}
.navbar-expand-md .navbar-nav .dropdown-menu{
	border-top:3px solid #fed136;
}
.dropdown-item:hover{background-color:#fed136;color:#fff;}
nav{-webkit-transition: padding-top .3s,padding-bottom .3s;
    -moz-transition: padding-top .3s,padding-bottom .3s;
    transition: padding-top .3s,padding-bottom .3s;
    border: none;
	}
</style>