<template>
  <header>
    <div class="header-wrapper">
      <div class="header-content">
        <div class="logo-wrapper">
          <img src="/src/assets/book.svg" alt="Book" class="book-icon" />
          <h2 class="logo">ElectoLibrary</h2>
        </div>

        <nav class="main-nav">
          <RouterLink to="/" active-class="active">Главная</RouterLink>
          <RouterLink to="/books" active-class="active">Каталог</RouterLink>
          <RouterLink to="/books/new" active-class="active">Добавить книгу</RouterLink>
        </nav>
      </div>
    </div>
  </header>
</template>

<style scoped>
header {
  width: 100%;
  padding: 0 20px;
  margin-bottom: 2rem;
}

.header-wrapper {
  width: 80%;
  margin: 0 auto;
  background: #e0f2fe;
  border-radius: 0 0 40px 40px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.8rem 2rem;
}

.logo-wrapper {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-wrapper h2 {
  margin: 0;                   
  color: #2c3e50;         
  font-size: 1.5rem;        
  line-height: 1;          
  letter-spacing: normal;   
}

.book-icon {
  width: 28px;
  height: 28px;
  display: block;
}

.logo {
  margin: 0;
  color: #153657;
  font-size: 1.5rem;
}

.main-nav {
  display: flex;
  gap: 0.5rem;
  background: transparent;
  padding: 0;
}

.main-nav a {
  color: #3b82f6;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  padding: 0.5rem 1.2rem;
  border-radius: 40px;
}

.main-nav a.active {
  color: #2c3e50;
}

.main-nav a:hover {
  color: #2c3e50;
}


@media (max-width: 768px) {
  .book-icon {
    width: 24px;
    height: 24px;
  }
  
  .logo {
    font-size: 1.2rem;
  }
}
</style>